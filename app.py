
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(20), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    occupied = db.Column(db.Integer, default=0, nullable=False)


class Allocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)


@app.route("/")
def home():
    students = Student.query.order_by(Student.name).all()
    rooms = Room.query.order_by(Room.room_number).all()
    allocations = Allocation.query.count()
    return render_template(
        "index.html",
        students=students,
        rooms=rooms,
        allocations=allocations,
    )


@app.route("/students", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    phone = request.form.get("phone", "").strip()

    if not name or not email or not phone:
        flash("Please complete all student fields.")
        return redirect(url_for("home"))

    try:
        if Student.query.filter_by(email=email).first():
            flash("This email is already registered.")
            return redirect(url_for("home"))

        db.session.add(Student(name=name, email=email, phone=phone))
        db.session.commit()
        flash("Student registered successfully.")
    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Student registration failed.")
        flash("Unable to register student.")

    return redirect(url_for("home"))


@app.route("/rooms", methods=["POST"])
def add_room():
    room_number = request.form.get("room_number", "").strip()
    try:
        capacity = int(request.form.get("capacity", "0"))
    except ValueError:
        capacity = 0

    if not room_number or capacity < 1:
        flash("Enter a room number and a valid capacity.")
        return redirect(url_for("home"))

    try:
        if Room.query.filter_by(room_number=room_number).first():
            flash("This room already exists.")
            return redirect(url_for("home"))

        db.session.add(Room(room_number=room_number, capacity=capacity))
        db.session.commit()
        flash("Room added successfully.")
    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Room creation failed.")
        flash("Unable to add room.")

    return redirect(url_for("home"))


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
