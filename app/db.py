from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class EnergyUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    energy_wh = db.Column(db.Float)
    voltage = db.Column(db.Float)
    current = db.Column(db.Float)
