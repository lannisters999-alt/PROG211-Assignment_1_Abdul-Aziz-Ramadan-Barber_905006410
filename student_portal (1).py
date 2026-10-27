"""
Student Learning Portal - Digital Public Goods (DPG) Compliant
Author: Limkokwing Student
Description: A modular Python program demonstrating OOP, a dictionary data
             structure, instance methods, and class methods for student
             record management.

DPG alignment:
- Open source: code is shared openly on GitHub.
- Privacy-respecting: only ID, name, age and major are stored.
  No contact details, grades or other sensitive data.
- Modular and reusable: each class has one clear job.
- Inclusive: plain-language messages that are easy to read and follow.
"""


class Student:
    """Represents one student record (non-sensitive data only)."""

    # Class attributes
    total_students = 0
    institution_name = "Limkokwing University of Creative Technology"

    def __init__(self, student_id, name, age, major):
        """Initializer to set up basic student attributes."""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    # ---------- Instance methods ----------
    def update_record(self, new_major):
        """Instance method to update an existing student's major/program."""
        if not new_major or not new_major.strip():
            print("-> Error: Major cannot be empty.")
            return False
        self.major = new_major.strip()
        print(f"-> Success: Record updated for Student ID {self.student_id}. "
              f"New major: {self.major}")
        return True

    def display_info(self):
        """Instance method to display individual student details."""
        print(f"   [ID: {self.student_id}] Name: {self.name}, "
              f"Age: {self.age}, Major: {self.major}")

    # ---------- Class methods ----------
    @classmethod
    def register(cls):
        """Class method: increase the count when a record is stored."""
        cls.total_students += 1

    @classmethod
    def unregister(cls):
        """Class method: decrease the count when a record is removed."""
        if cls.total_students > 0:
            cls.total_students -= 1

    @classmethod
    def get_total_students(cls):
        """Class method: return the total number of stored students."""
        return cls.total_students


class StudentManager:
    """Manages Student objects using a Python dictionary."""

    def __init__(self):
        # Dictionary: unique student ID (key) -> Student object (value)
        self.records = {}

    @staticmethod
    def _is_valid(student_id, name, age, major):
        """Check the input and print a clear message if something is wrong."""
        if not isinstance(student_id, str) or not student_id.strip():
            print("-> Error: Student ID must be a non-empty text value.")
            return False
        if not isinstance(name, str) or not name.strip():
            print("-> Error: Name cannot be empty.")
            return False
        if isinstance(age, bool) or not isinstance(age, int) or not 1 <= age <= 120:
            print("-> Error: Age must be a whole number between 1 and 120.")
            return False
        if not isinstance(major, str) or not major.strip():
            print("-> Error: Major cannot be empty.")
            return False
        return True

    def add_record(self, student_id, name, age, major):
        """Add a new student record into the dictionary."""
        if not self._is_valid(student_id, name, age, major):
            return False
        if student_id in self.records:
            print(f"-> Error: Student ID {student_id} already exists.")
            return False

        self.records[student_id] = Student(student_id, name.strip(), age, major.strip())
        Student.register()  # count only records that are really stored
        print(f"-> Success: Student {name.strip()} added successfully.")
        return True

    def find_record(self, student_id):
        """Return the Student object for an ID, or None if not found."""
        return self.records.get(student_id)

    def remove_record(self, student_id):
        """Remove a student record from the dictionary."""
        if student_id not in self.records:
            print(f"-> Error: Student ID {student_id} not found.")
            return False
        removed = self.records.pop(student_id)
        Student.unregister()
        print(f"-> Success: Record for {removed.name} (ID {student_id}) removed.")
        return True

    def display_records(self):
        """Display all records stored in the dictionary."""
        if not self.records:
            print("-> No student records found in the system.")
            return
        print("\n--- CURRENT STUDENT RECORDS ---")
        for student_obj in self.records.values():
            student_obj.display_info()
        print("-------------------------------\n")


# --- EXAMPLE USAGE & PROGRAM EXECUTION ---
if __name__ == "__main__":
    print("=== INITIALIZING LIMKOKWING EDUCATION DPG PORTAL ===\n")

    manager = StudentManager()

    # 1. Adding records
    manager.add_record("S001", "Aminata Conteh", 20, "Information Technology")
    manager.add_record("S002", "Mohamed Kamara", 22, "Software Engineering")
    manager.add_record("S003", "Fatmata Sesay", 21, "Multimedia Design")

    # 2. Error handling demonstration
    print("\n-> Testing error handling:")
    manager.add_record("S001", "Duplicate Person", 25, "Business")  # duplicate ID
    manager.add_record("S004", "Invalid Age", -5, "Business")       # bad age

    # 3. Displaying all records
    manager.display_records()

    # 4. Instance method: update a record
    print("-> Updating a record using an instance method...")
    manager.records["S001"].update_record("Cyber Security")

    # 5. Find and display one student
    print("\n-> Displaying info for a specific student:")
    student = manager.find_record("S001")
    if student:
        student.display_info()

    # 6. Remove a record
    print("\n-> Removing a record:")
    manager.remove_record("S003")
    manager.remove_record("S999")  # does not exist

    # 7. Class method: total students
    print("\n-> Accessing class method:")
    total = Student.get_total_students()
    print(f"-> [System Stat] Total Registered Students at "
          f"{Student.institution_name}: {total}")

    manager.display_records()

    print("=== SYSTEM SHUTDOWN. ONLY NON-SENSITIVE DATA STORED. ===")
