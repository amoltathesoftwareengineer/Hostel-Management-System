
-- Hostel Management System
-- SQLite database schema

CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS room (
    id INTEGER PRIMARY KEY,
    room_number VARCHAR(20) NOT NULL UNIQUE,
    capacity INTEGER NOT NULL CHECK (capacity >= 1),
    occupied INTEGER NOT NULL DEFAULT 0,
    CHECK (occupied >= 0 AND occupied <= capacity)
);

CREATE TABLE IF NOT EXISTS allocation (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (room_id) REFERENCES room(id)
);
