from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

db = SQLAlchemy()

class FitnessClass(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    instructor = db.Column(db.String(50), nullable=False)
    available_slots = db.Column(db.Integer, nullable=False)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    client_name = db.Column(db.String(50), nullable=False)
    client_email = db.Column(db.String(120), nullable=False)

    fitness_class = db.relationship('FitnessClass', backref=db.backref('bookings', lazy=True))
