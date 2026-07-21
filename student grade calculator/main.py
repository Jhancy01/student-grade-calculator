"""
main.py
--------
Entry point for the Student Grade Calculator application.

This file is responsible ONLY for:
    - Displaying the menu
    - Reading the user's menu choice
    - Calling the appropriate functions from grade_calculator.py

All calculation, validation, and file-handling logic lives in
grade_calculator.py, keeping this file short and easy to follow.

Run this file to start the application:
    python main.py
"""

import grade_calculator as gc


def process_new_student():
    """
    Collect a new student's details and marks, calculate their
    total/average/grade, display the report card, and save the
    record to the CSV file.
    """
    print("\n--- Enter Student Details ---")

    # Step 1: Collect basic student information.
    name = gc.get_non_empty_string("Enter Student Name: ")
    roll_number = gc.get_valid_roll_number()

    # Step 2: Collect and validate marks for each subject.
    marks = []
    for subject_number in range(1, gc.NUM_SUBJECTS + 1):
        mark = gc.get_valid_mark(subject_number)
        marks.append(mark)

    # Step 3: Perform calculations.
    total = gc.calculate_total(marks)
    average = gc.calculate_average(total)
    grade = gc.calculate_grade(average)

    # Step 4: Bundle everything into a single student record (dict).
    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade,
    }

    # Step 5: Show the report card to the user.
    gc.print_report_card(student)

    # Step 6: Save the record to the CSV file.
    if gc.save_student_record(student):
        print(f"Record for '{name}' saved successfully to {gc.DATA_FILE}.\n")
    else:
        print("Something went wrong while saving the record.\n")


def show_menu():
    """Display the main menu options to the user."""
    print("=" * 40)
    print("     STUDENT GRADE CALCULATOR")
    print("=" * 40)
    print("1. Add New Student & Calculate Grade")
    print("2. View All Saved Records")
    print("3. Exit")
    print("=" * 40)


def main():
    """
    Main application loop.
    Repeatedly shows the menu and handles the user's selection until
    they choose to exit.
    """
    while True:
        show_menu()
        try:
            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                process_new_student()
            elif choice == "2":
                gc.display_all_records()
            elif choice == "3":
                print("\nThank you for using Student Grade Calculator. Goodbye!")
                break
            else:
                print("\nInvalid choice! Please enter a number between 1 and 3.\n")

        except KeyboardInterrupt:
            # Gracefully handle Ctrl+C interruption.
            print("\n\nProgram interrupted by user. Exiting gracefully...")
            break
        except Exception as error:
            # Catch-all safety net so the app never crashes unexpectedly.
            print(f"\nAn unexpected error occurred: {error}\n")


# Standard Python entry-point guard.
# Ensures main() only runs when this file is executed directly,
# not when it is imported as a module elsewhere.
if __name__ == "__main__":
    main()
