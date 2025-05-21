from flask import Blueprint, render_template, jsonify, redirect, url_for
from .db import db, EnergyUsage
from .tinytuya_api import get_device_status, set_device_power
import json
from datetime import datetime

bp = Blueprint('main', __name__)

with open('devices.json') as f:
    DEVICES = json.load(f)

def get_device_name(dev_id):
    return next((d['name'] for d in DEVICES if d['id'] == dev_id), dev_id)

@bp.route('/')
def dashboard():
    data = EnergyUsage.query.order_by(EnergyUsage.timestamp.desc()).limit(20).all()
    latest = {d['id']: get_device_status(d['id'], d['ip'], d['key']) for d in DEVICES}
    cost_estimates = {}
    for device_id, metrics in latest.items():
        power_w = metrics['power']
        cost_estimates[device_id] = round((power_w / 1000) * 9, 2)
    return render_template('dashboard.html', data=data, devices=DEVICES, latest=latest, costs=cost_estimates)

@bp.route('/refresh')
def refresh():
    all_status = []
    for device in DEVICES:
        try:
            status = get_device_status(device['id'], device['ip'], device['key'])
            usage = EnergyUsage(
                device_id=device['id'],
                power=status['power'],
                voltage=status['voltage'],
                current=status['current']
            )
            db.session.add(usage)
            print(status)
            all_status.append({"device_id": device['id'], **status})
        except Exception as e:
            all_status.append({"device_id": device['id'], "error": str(e)})
    db.session.commit()
    return jsonify({"status": "updated", "data": all_status})

@bp.route('/device/<device_id>')
def device_page(device_id):
    history = EnergyUsage.query.filter_by(device_id=device_id).order_by(EnergyUsage.timestamp.desc()).limit(100).all()
    device_name = get_device_name(device_id)
    return render_template('device.html', history=history, device_id=device_id, device_name=device_name)

@bp.route('/toggle/<device_id>/<state>')
def toggle_device(device_id, state):
    device = next((d for d in DEVICES if d['id'] == device_id), None)
    if device:
        set_device_power(device_id, device['ip'], device['key'], state.lower() == 'on')
    return redirect(url_for('main.dashboard'))
