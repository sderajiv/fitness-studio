from models import db, FitnessClass
from datetime import datetime, timedelta
import pytz
import sqlite3

def convert_to_timezone(dt_obj, target_timezone):
    target_tz = pytz.timezone(target_timezone)
    ist = pytz.timezone('Asia/Kolkata')
    if dt_obj.tzinfo is None:
        dt_obj = ist.localize(dt_obj)
    return dt_obj.astimezone(target_tz).isoformat()



def seed_classes(app):
    with app.app_context():
        if FitnessClass.query.first():
            return

        ist = pytz.timezone('Asia/Kolkata')
        now_ist = datetime.now(ist)

        data = [
            FitnessClass(
                name="Yoga",
                datetime=now_ist + timedelta(days=1),
                instructor="Riya Sharma",  
                available_slots=10
            ),
            FitnessClass(
                name="Zumba",
                datetime=now_ist + timedelta(days=2),
                instructor="Aman Verma",  
                available_slots=8
            ),
            FitnessClass(
                name="HIIT",
                datetime=now_ist + timedelta(days=3),
                instructor="Neha Mehta",  
                available_slots=5
            ),
        ]

        db.session.bulk_save_objects(data)
        db.session.commit()