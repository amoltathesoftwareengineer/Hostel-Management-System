# Hostel Management System

A database-driven web application built with Python and Flask to manage student registrations, hostel rooms, and room allocations.

## Features

- **Student Registration** — Register students with their name, email, and phone number.
- **Room Management** — Add hostel rooms and define their capacity.
- **Room Allocation** — Assign available rooms to registered students.
- **Capacity Validation** — Prevent room allocation when a room is full.
- **Duplicate Prevention** — Prevent duplicate student emails and room numbers.
- **Dashboard Statistics** — View student counts, total rooms, and room allocations.
- **Health Check API** — Check application status through `/health`.
- **Automated Testing** — Run tests with pytest and GitHub Actions.

## Technology Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **ORM:** Flask-SQLAlchemy
- **Frontend:** HTML5, CSS3, Jinja2
- **Testing:** pytest
- **CI:** GitHub Actions

## Project Structure

```text
Hostel-Management-System/
├── .github/
│   └── workflows/
│       └── tests.yml
├── templates/
│   └── index.html
├── tests/
│   └── test_app.py
├── app.py
├── config.py
├── database.sql
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or later
- pip

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/amoltathesoftwareengineer/Hostel-Management-System.git
   ```

2. Open the project directory:

   ```bash
   cd Hostel-Management-System
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment on Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS or Linux:

   ```bash
   source venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   python app.py
   ```

7. Open the local application in your browser:

   `http://127.0.0.1:5000`

## Running Tests

Run the following command from the project directory:

```bash
python -m pytest -v
```

## Health Check

Visit the following endpoint while the application is running:

`http://127.0.0.1:5000/health`

A successful response returns:

```json
{
  "status": "healthy"
}
```

## Database

The application uses SQLite through Flask-SQLAlchemy. Database tables are created automatically when the application starts.

The `database.sql` file contains a standalone SQLite schema for reference.

## Future Enhancements

- Student room transfer and room vacancy management
- Fee tracking and payment records
- Maintenance request management
- Role-based authentication and authorization
- Occupancy analytics and downloadable reports

## Author

**Amol Tathe**

- GitHub: [@amoltathesoftwareengineer](https://github.com/amoltathesoftwareengineer)

---

*This project is intended for learning and demonstration. Authentication, authorization, production security configuration, and additional operational features are needed before production deployment.*
