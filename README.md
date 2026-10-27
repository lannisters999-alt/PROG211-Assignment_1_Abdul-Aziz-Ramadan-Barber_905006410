# Student Learning Portal (DPG-Compliant)

A simple, modular Python program for managing student records. It was built for the Python Object-Oriented Programming assignment (Semester 3, ICT) at Limkokwing University of Creative Technology, Sierra Leone, and follows Digital Public Goods (DPG) principles.

**Domain:** Education
**Language:** Python 3 (no external libraries needed)

---

## Problem Statement

Schools often track student information on paper, which is slow, easy to lose, and hard to update. This program shows how a small, open-source tool can store, find, update, and remove basic student records in an organised way, using only non-sensitive data.

---

## Features

- Add student records (with input validation and duplicate-ID protection)
- Display all records
- Find a student by ID
- Update a student's major (program)
- Remove a student record
- Track the total number of registered students

---

## Project Structure

```
student-learning-portal/
├── student_portal.py   # Main program (classes + example usage)
└── README.md           # Documentation
```

---

## How It Works

### Classes

| Class | Purpose |
|---|---|
| `Student` | Represents one student with `student_id`, `name`, `age`, and `major`. |
| `StudentManager` | Manages all students using a dictionary. |

### Data Structure

A single **dictionary** stores all records: the student ID is the key (unique) and the `Student` object is the value. Lookups by ID are fast and duplicate IDs are rejected.

### Methods

| Type | Method | What it does |
|---|---|---|
| Instance method | `update_record(new_major)` | Updates a student's major |
| Instance method | `display_info()` | Prints one student's details |
| Class method | `get_total_students()` | Returns the total number of stored students |
| Class method | `register()` / `unregister()` | Adds to / subtracts from the total count |
| Manager function | `add_record(...)` | Validates and adds a record |
| Manager function | `display_records()` | Displays all records |
| Manager function | `find_record(id)` | Returns a student or `None` |
| Manager function | `remove_record(id)` | Removes a record |

---

## DPG Alignment

| DPG Principle | How this project meets it |
|---|---|
| **Open source** | The code is shared openly on GitHub so anyone can read, use, improve, and reuse it. |
| **Inclusive and accessible** | The program is text-based and runs on any computer with Python, with no internet, special hardware, or paid software. Messages are written in plain, simple English. |
| **Privacy-respecting** | Only four non-sensitive fields are stored: ID, name, age, and major. No contact details, addresses, grades, or health information are collected. |
| **Modular and reusable** | Each class has one clear job, so the code can be reused or extended (for example, by adding a database or a web interface). |

---

## How to Run

1. Install Python 3 from https://www.python.org
2. Download or clone this repository:
   ```
   git clone <your-repository-link>
   cd student-learning-portal
   ```
3. Run the program:
   ```
   python student_portal.py
   ```

---

## Example Usage

**Sample code:**

```python
manager = StudentManager()
manager.add_record("S001", "Aminata Conteh", 20, "Information Technology")
manager.add_record("S002", "Mohamed Kamara", 22, "Software Engineering")
manager.display_records()
manager.records["S001"].update_record("Cyber Security")
print(Student.get_total_students())
```

**Sample output (from running `student_portal.py`):**

```
=== INITIALIZING LIMKOKWING EDUCATION DPG PORTAL ===

-> Success: Student Aminata Conteh added successfully.
-> Success: Student Mohamed Kamara added successfully.
-> Success: Student Fatmata Sesay added successfully.

-> Testing error handling:
-> Error: Student ID S001 already exists.
-> Error: Age must be a whole number between 1 and 120.

--- CURRENT STUDENT RECORDS ---
   [ID: S001] Name: Aminata Conteh, Age: 20, Major: Information Technology
   [ID: S002] Name: Mohamed Kamara, Age: 22, Major: Software Engineering
   [ID: S003] Name: Fatmata Sesay, Age: 21, Major: Multimedia Design
-------------------------------

-> Updating a record using an instance method...
-> Success: Record updated for Student ID S001. New major: Cyber Security

-> Displaying info for a specific student:
   [ID: S001] Name: Aminata Conteh, Age: 20, Major: Cyber Security

-> Removing a record:
-> Success: Record for Fatmata Sesay (ID S003) removed.
-> Error: Student ID S999 not found.

-> Accessing class method:
-> [System Stat] Total Registered Students at Limkokwing University of Creative Technology: 2

--- CURRENT STUDENT RECORDS ---
   [ID: S001] Name: Aminata Conteh, Age: 20, Major: Cyber Security
   [ID: S002] Name: Mohamed Kamara, Age: 22, Major: Software Engineering
-------------------------------

=== SYSTEM SHUTDOWN. ONLY NON-SENSITIVE DATA STORED. ===
```

---

## Future Improvements

- Save records to a file or database so they are kept after the program closes
- Add a simple menu so users can type their own records
- Add a web or mobile interface

---

## Author

Student, Limkokwing University of Creative Technology (Sierra Leone)
ICT Semester 3, Python OOP and Digital Public Goods Assignment

## License

Released under the MIT License. Free to use, modify, and share.
