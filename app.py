from flask import Flask, request, jsonify
from models import db, FitnessClass, Booking
from utils import convert_to_timezone, seed_classes
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
    seed_classes(app)


import os
print("Using DB at:", os.path.abspath(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')))



@app.route('/get_classes', methods=['GET'])
def get_classes():
    timezone = request.args.get('tz', 'Asia/Kolkata')
    classes = FitnessClass.query.all()
    result = [{
        "id": c.id,
        "name": c.name,
        "datetime": convert_to_timezone(c.datetime, timezone),
        "instructor": c.instructor,
        "available_slots": c.available_slots
    } for c in classes]
    return jsonify(result)
@app.route('/book_class', methods=['POST'])
def book_class():
    data = request.get_json()
    required = ['class_id', 'client_name', 'client_email']
    if not data or not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    fitness_class = FitnessClass.query.get(data['class_id'])
    if not fitness_class:
        return jsonify({"error": "Class not found"}), 404

    if fitness_class.available_slots <= 0:
        return jsonify({"error": "Class is fully booked"}), 400

    existing = Booking.query.filter_by(
        class_id=data['class_id'],
        client_email=data['client_email']
    ).first()

    if existing:
        return jsonify({"error": "You have already booked this class"}), 400

    booking = Booking(
        class_id=data['class_id'],
        client_name=data['client_name'],
        client_email=data['client_email']
    )
    fitness_class.available_slots -= 1
    db.session.add(booking)
    db.session.commit()

    return jsonify({"message": "Booking successful"}), 201

@app.route('/get_bookings', methods=['GET'])
def get_bookings():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email query param is required"}), 400

    bookings = Booking.query.filter_by(client_email=email).all()
    if not bookings:
        return jsonify({"message": f"No bookings found for email: {email}"}), 404

    result = [{
        "booking_id": b.id,
        "class": b.fitness_class.name,
        "datetime": b.fitness_class.datetime.isoformat(),
        "instructor": b.fitness_class.instructor
    } for b in bookings]
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
