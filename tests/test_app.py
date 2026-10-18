
import unittest

from app import app, db, Student, Room


class HostelManagementTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}

        self.context = app.app_context()
        self.context.push()

        db.drop_all()
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hostel Management System", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "healthy"})

    def test_student_registration(self):
        response = self.client.post("/students", data={
            "name": "Test Student",
            "email": "student@example.com",
            "phone": "9876543210",
        })
        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(
            Student.query.filter_by(email="student@example.com").first()
        )

    def test_room_creation(self):
        response = self.client.post("/rooms", data={
            "room_number": "A101",
            "capacity": "3",
        })
        self.assertEqual(response.status_code, 302)
        room = Room.query.filter_by(room_number="A101").first()
        self.assertIsNotNone(room)
        self.assertEqual(room.capacity, 3)


if __name__ == "__main__":
    unittest.main()
