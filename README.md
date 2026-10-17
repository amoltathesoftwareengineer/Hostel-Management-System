# Hostel Management System

A database-driven application for managing hostel operations, student accommodation, room assignments, and hostel administration.

## Overview

The Hostel Management System centralizes hostel records and helps administrators manage student details, room availability, allocation, fee records, and maintenance requests.

## Key Features

- Student registration and profile management
- Hostel and room management
- Room availability tracking
- Room allocation and transfer records
- Fee payment status tracking
- Attendance records
- Maintenance request management
- Administrative reports
- Role-based access control

## Technology Stack

- Python
- Flask
- MySQL 8.0
- HTML5 and CSS3
- Bootstrap
- Jinja2

## Database Design

Proposed tables:

- `students`
- `hostels`
- `rooms`
- `room_allocations`
- `fee_records`
- `attendance`
- `maintenance_requests`
- `users`

Use foreign keys and validation rules to prevent invalid allocations and inconsistent records.

## Project Structure

```text
Hostel-Management-System/
├── app.py
├── config.py
├── database.sql
├── requirements.txt
├── README.md
├── templates/
├── static/
└── tests/
```

## Installation

```bash
git clone https://github.com/amoltathesoftwareengineer/Hostel-Management-System.git
cd Hostel-Management-System
python -m venv .venv
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure MySQL, execute `database.sql`, and set the required environment variables.

## Run the Application

```bash
python app.py
```

Open the local development URL displayed in the terminal.

## Database and Security

- Enforce room capacity limits.
- Prevent overlapping active allocations.
- Use parameterized SQL queries.
- Hash user passwords securely.
- Restrict administrative operations.
- Protect students' personal information.

## Future Enhancements

- Online fee payment integration
- Room availability dashboard
- Visitor management
- Maintenance notifications
- Occupancy analytics
- Downloadable reports

## Author

Amol Tathe

GitHub: https://github.com/amoltathesoftwareengineer

## License

Add an appropriate open-source license before permitting reuse.
