Event Management System - Backend

A Flask REST API backend for an Event Management System. This backend allows users to create accounts, log in, and manage events securely using Flask, SQLAlchemy, Flask-Migrate, and SQLite.

Features
User registration and authentication
User login/logout with sessions
Password hashing using Flask-Bcrypt
Create, read, update, and delete events
User-specific event management
Database migrations with Flask-Migrate
RESTful API endpoints
CORS support for frontend connection
Technologies Used
Python 3
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-Bcrypt
Flask-CORS
SQLite
Gunicorn (production server)
Project Structure
Event-management-system-BACKEND/
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── models/
│   ├── user.py
│   └── event.py
├── routes/
│   ├── auth.py
│   └── events.py
├── migrations/
└── seed.py
Installation

Clone the repository:

git clone https://github.com/preciousrodenyi-ctrl/Event-management-system-BACKEND.git

Move into the project folder:

cd Event-management-system-BACKEND

Create a virtual environment:

python -m venv venv

Activate it:

Linux/Mac
source venv/bin/activate
Windows
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Environment Variables

Create a .env file:

SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///eventhub.db
Database Setup

Initialize migrations:

flask db init

Run migrations:

flask db migrate
flask db upgrade

Seed sample data:

python seed.py
Running the Application

Start the Flask development server:

python app.py

The API will run at:

http://127.0.0.1:5555
API Endpoints
Authentication
Register User

POST

/api/signup

Example:

{
  "username": "Precious",
  "email": "precious@example.com",
  "password": "password123"
}
Login User

POST

/api/login

Example:

{
  "email": "precious@example.com",
  "password": "password123"
}
Check Login Session

GET

/api/check_session
Events
Get Events

GET

/api/events
Create Event

POST

/api/events

Example:

{
  "title": "Tech Meetup",
  "description": "A developer networking event",
  "location": "Nairobi",
  "date": "2026-08-01",
  "category": "Technology"
}
Update Event

PUT

/api/events/<id>
Delete Event

DELETE

/api/events/<id>
Deployment

This project is deployed using Render.

Production server:

gunicorn app:app

Live API:

https://event-management-system-backend-tjsl.onrender.com
Frontend Connection

The frontend application connects to this API using Axios.

Frontend repository:

Event-management-system-FRONTEND
Author

Precious Rodenyi

GitHub:

https://github.com/preciousrodenyi-ctrl

License

This project is for educational purposes.