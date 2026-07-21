# 🎓 Student Grade Calculator

A simple, menu-driven **console application** built in Python that calculates
a student's total marks, average percentage, and letter grade — then saves
the record to a CSV file for future reference.

This project is designed to be **beginner-friendly**, **modular**, and a
great addition to a Python portfolio.

---

## 📋 Project Description

The Student Grade Calculator asks the user for a student's name, roll
number, and marks in 5 subjects. It validates the input, calculates the
total marks, average percentage, and letter grade, then displays a
formatted report card. All records are saved to a CSV file (`data.csv`)
so they can be viewed again later — even after the program is closed.

---

## ✨ Features

- 📝 Menu-driven interface (Add Student / View Records / Exit)
- ✅ Input validation (marks must be numeric and between 0–100)
- 🧮 Automatic calculation of Total Marks, Average %, and Grade
- 🏆 Grade system based on standard percentage bands
- 🖥️ Clean, well-formatted report card output
- 💾 Persistent storage using CSV (`data.csv`)
- 📊 View all previously saved student records in a table
- 🛡️ Robust error handling with `try-except` throughout
- 🧩 Modular code split across `main.py` and `grade_calculator.py`
- 📐 Follows PEP 8 coding standards

---

## 🛠️ Technologies Used

- **Python 3** (standard library only)
- `csv` module — for reading/writing student records
- `os` module — for checking file existence

No external/third-party packages are required.

---

## 📂 Project Structure

```
Student-Grade-Calculator/
│── main.py               # Entry point — menu & user interaction
│── grade_calculator.py    # Core logic — validation, calculations, CSV I/O
│── data.csv               # Stores saved student records
│── README.md              # Project documentation (this file)
│── requirements.txt       # Project dependencies (none — stdlib only)
│── LICENSE                # MIT License
│── .gitignore             # Files/folders excluded from version control
```

---

## ⚙️ Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Student-Grade-Calculator.git
   cd Student-Grade-Calculator
   ```

2. **Ensure Python 3 is installed**
   ```bash
   python3 --version
   ```
   (Requires Python 3.7 or higher)

3. **(Optional) Install dependencies**
   This project uses only Python's standard library, so no installation
   is required. `requirements.txt` is included for completeness.
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ How to Run

Run the application from the project folder:

```bash
python main.py
```

or, depending on your system setup:

```bash
python3 main.py
```

You'll then see the main menu:

```
========================================
     STUDENT GRADE CALCULATOR
========================================
1. Add New Student & Calculate Grade
2. View All Saved Records
3. Exit
========================================
Enter your choice (1-3):
```

---

## 🖼️ Sample Output

**Adding a new student:**

```
--- Enter Student Details ---
Enter Student Name: John Doe
Enter Roll Number: 101
Enter marks for Subject 1 (0-100): 95
Enter marks for Subject 2 (0-100): 88
Enter marks for Subject 3 (0-100): 76
Enter marks for Subject 4 (0-100): 92
Enter marks for Subject 5 (0-100): 85

========================================
             STUDENT REPORT CARD
========================================
Name        : John Doe
Roll Number : 101
----------------------------------------
Subject 1    : 95.00
Subject 2    : 88.00
Subject 3    : 76.00
Subject 4    : 92.00
Subject 5    : 85.00
----------------------------------------
Total Marks : 436.00 / 500
Average (%) : 87.20%
Grade       : A
========================================

Record for 'John Doe' saved successfully to data.csv.
```

**Viewing all records:**

```
====================================================================================================
                                   ALL STUDENT RECORDS
====================================================================================================
Name           Roll Number Subject1  Subject2  Subject3  Subject4  Subject5  Total Marks Average (%) Grade
----------------------------------------------------------------------------------------------------
John Doe       101         95.00     88.00     76.00     92.00     85.00     436.00      87.20       A
====================================================================================================
```

---

## 🏆 Grade Scale

| Percentage Range | Grade |
|-------------------|-------|
| 90 – 100           | A+    |
| 80 – 89            | A     |
| 70 – 79            | B     |
| 60 – 69            | C     |
| 50 – 59            | D     |
| Below 50           | F     |

---

## 🚀 Future Improvements

- Add a graphical user interface (GUI) using Tkinter or PyQt
- Add search/filter/delete functionality for existing records
- Export report cards as PDF files
- Add support for a variable number of subjects
- Add unit tests using `pytest`
- Add subject names/weightage instead of generic "Subject 1..5"
- Add data visualization (e.g., grade distribution charts)
- Support multiple classes/sections with separate CSV files

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — feel free to
use, modify, and share it.
