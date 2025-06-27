# Fitness Studio Booking API

This is a basic Flask application that provides API endpoints for managing class bookings in a fitness studio. The studio offers classes like Yoga, Zumba, and HIIT. Users can view available classes, book them, and check bookings by email.

## Features

Get list of available classes
Book a class if slots are available
View bookings using email
Timezone support for class timings
Data stored using SQLite and SQLAlchemy ORM
Auto seed data when app starts

---

## Tech Used

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- Pytz

---

## How to Set Up

1. Clone the repo or copy files into a folder  
2. Make sure Python 3 is installed  
3. Open terminal in the project folder  


2. Install Required Packages
bash
pip install -r requirements.txt

3. Run Migrations and Start App
flask db init
flask db migrate -m "initial"
flask db upgrade
flask run


API Endpoints

1. Get All Classes
GET /get_classes

2. Book a Class
POST /book_class
{
  "class_id": 1,
  "client_name": "Sonu",
  "client_email": "sonu@gmail.com"
}

3. Get Bookings by Email
GET /get_bookings?email=enter booked client_email

Postman Collection also there just download import and use locally

cheked loom video link
https://www.loom.com/share/c48f45287608491eafba126f14e178f8?sid=a5bb4d60-1eca-4b15-bba9-665bf02b0c37
