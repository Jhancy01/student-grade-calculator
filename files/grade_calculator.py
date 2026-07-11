"""
grade_calculator.py
--------------------
This module contains all the "business logic" for the Student Grade
Calculator application:

    - Input validation helpers
    - Grade / total / average calculations
    - CSV file read & write operations
    - Report card formatting/printing

Keeping this logic separate from main.py (which only handles the menu
and user interaction) makes the code modular, easier to test, and
easier to maintain.
"""

import csv
import os

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Name of the CSV file where student records are stored.
DATA_FILE = "data.csv"

# Column headers used in the CSV file.
CSV_HEADERS = [
    "Name",
    "Roll Number",
    "Subject1",
    "Subject2",
    "Subject3",
    "Subject4",
    "Subject5",
    "Total Marks",
    "Average (%)",
    "Grade",
]

# Number of subjects each student is graded on.
NUM_SUBJECTS = 5


# ---------------------------------------------------------------------------
# Input validation helpers
# ---------------------------------------------------------------------------

def get_non_empty_string(prompt):
    """
    Keep asking the user for input until a non-empty string is given.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        str: A non-empty, stripped string entered by the user.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_valid_mark(subject_number):
    """
    Ask the user for a single subject's marks and validate that the
    value is a number between 0 and 100 (inclusive).

    Args:
        subject_number (int): The subject index (used for the prompt).

    Returns:
        float: A validated mark between 0 and 100.
    """
    while True:
        try:
            mark = float(input(f"Enter marks for Subject {subject_number} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Invalid marks! Please enter a value between 0 and 100.")
        except ValueError:
            # Raised when the user enters non-numeric input.
            print("Invalid input! Please enter a numeric value.")


def get_valid_roll_number():
    """
    Ask the user for a roll number and validate that it is a positive
    whole number.

    Returns:
        str: The validated roll number (kept as a string since it is
             used only as an identifier, not for arithmetic).
    """
    while True:
        try:
            roll = int(input("Enter Roll Number: "))
            if roll > 0:
                return str(roll)
            print("Roll number must be a positive integer.")
        except ValueError:
            print("Invalid input! Roll number must be a whole number.")


# ---------------------------------------------------------------------------
# Core calculations
# ---------------------------------------------------------------------------

def calculate_total(marks):
    """
    Calculate the total marks scored across all subjects.

    Args:
        marks (list[float]): List of marks for each subject.

    Returns:
        float: Sum of all marks.
    """
    return sum(marks)


def calculate_average(total, num_subjects=NUM_SUBJECTS):
    """
    Calculate the average percentage.

    Args:
        total (float): Total marks scored.
        num_subjects (int): Number of subjects (default 5).

    Returns:
        float: Average percentage rounded to 2 decimal places.
    """
    average = total / num_subjects
    return round(average, 2)


def calculate_grade(average):
    """
    Determine the letter grade based on the average percentage.

    Grade Scale:
        A+ : 90-100
        A  : 80-89
        B  : 70-79
        C  : 60-69
        D  : 50-59
        F  : Below 50

    Args:
        average (float): The average percentage.

    Returns:
        str: The letter grade.
    """
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# ---------------------------------------------------------------------------
# Report card display
# ---------------------------------------------------------------------------

def print_report_card(student):
    """
    Print a neatly formatted report card for a single student.

    Args:
        student (dict): Dictionary containing student details, marks,
                         total, average, and grade.
    """
    print("\n" + "=" * 40)
    print("             STUDENT REPORT CARD")
    print("=" * 40)
    print(f"Name        : {student['name']}")
    print(f"Roll Number : {student['roll_number']}")
    print("-" * 40)

    for index, mark in enumerate(student["marks"], start=1):
        print(f"Subject {index}    : {mark:.2f}")

    print("-" * 40)
    print(f"Total Marks : {student['total']:.2f} / {NUM_SUBJECTS * 100}")
    print(f"Average (%) : {student['average']:.2f}%")
    print(f"Grade       : {student['grade']}")
    print("=" * 40 + "\n")


# ---------------------------------------------------------------------------
# CSV file operations
# ---------------------------------------------------------------------------

def save_student_record(student):
    """
    Append a single student's record to the CSV data file.
    Creates the file (with headers) if it does not already exist.

    Args:
        student (dict): Dictionary containing student details, marks,
                         total, average, and grade.

    Returns:
        bool: True if the record was saved successfully, False otherwise.
    """
    file_exists = os.path.isfile(DATA_FILE)

    try:
        with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            # Write the header row only once, when creating a new file.
            if not file_exists:
                writer.writerow(CSV_HEADERS)

            row = [
                student["name"],
                student["roll_number"],
                *[f"{m:.2f}" for m in student["marks"]],
                f"{student['total']:.2f}",
                f"{student['average']:.2f}",
                student["grade"],
            ]
            writer.writerow(row)
        return True

    except (IOError, OSError) as error:
        print(f"Error saving record to file: {error}")
        return False


def load_all_records():
    """
    Read all student records from the CSV data file.

    Returns:
        list[list[str]]: A list of rows (including the header row) from
                          the CSV file. Returns an empty list if the
                          file does not exist or cannot be read.
    """
    if not os.path.isfile(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            return list(reader)
    except (IOError, OSError) as error:
        print(f"Error reading file: {error}")
        return []


def display_all_records():
    """
    Print all saved student records in a neatly formatted table.
    Shows a friendly message if no records are found.
    """
    records = load_all_records()

    if not records:
        print("\nNo student records found yet. Add a student first!\n")
        return

    header, *rows = records

    print("\n" + "=" * 100)
    print("                                   ALL STUDENT RECORDS")
    print("=" * 100)

    # Print header row.
    print(
        f"{header[0]:<15}{header[1]:<12}"
        f"{header[2]:<10}{header[3]:<10}{header[4]:<10}{header[5]:<10}{header[6]:<10}"
        f"{header[7]:<12}{header[8]:<12}{header[9]:<8}"
    )
    print("-" * 100)

    # Print each student's row.
    for row in rows:
        print(
            f"{row[0]:<15}{row[1]:<12}"
            f"{row[2]:<10}{row[3]:<10}{row[4]:<10}{row[5]:<10}{row[6]:<10}"
            f"{row[7]:<12}{row[8]:<12}{row[9]:<8}"
        )

    print("=" * 100 + "\n")
