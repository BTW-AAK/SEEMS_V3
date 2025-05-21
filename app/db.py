from flask_sqlalchemy import SQLAlchemy
import datetime
import pytz

db = SQLAlchemy()
ist_timezone = pytz.timezone('Asia/Kolkata')

class EnergyUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now(ist_timezone))
    energy_wh = db.Column(db.Float)
    voltage = db.Column(db.Float)
    current = db.Column(db.Float)
