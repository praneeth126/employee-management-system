# Employee Management System

A command-line based Employee Management System built using **Python and MySQL**. The application provides full CRUD operations, input and duplicate validation, and a built-in SQL analytics module for workforce metrics.

---

## Features

- **Employee Records Management (CRUD)**
  - View all employee records in formatted profiles.
  - Add new employees with duplicate checking on ID and email.
  - Search employees by exact ID or case-insensitive partial name match.
  - Update employee details field-by-field, including Name, Age, Gender, Phone, Email, Address, Department, Designation, Salary, and Joining Date.
  - Delete employee records with confirmation safeguard.

- **Input Validation & Data Integrity**
  - Duplicate detection for `employee_id` and unique `email` addresses.
  - Age restriction between 18 and 100 years.
  - Phone format validation.
  - Email format validation.
  - Numeric validation for IDs and salary values.
  - Date validation using `YYYY-MM-DD` format.

- **Workforce Analytics**
  - Total employee headcount and gender distribution.
  - Department and designation employee counts.
  - Overall salary metrics: average, maximum, and minimum.
  - Department-wise average salary.
  - Department-wise salary analysis.
  - Highest-paying department based on average salary.
  - Salary tier classification.
  - Employee joining statistics grouped by joining year.

- **Security & Reliability**
  - Database credentials managed through `.env` using `python-dotenv`.
  - Parameterized SQL queries to help protect against SQL injection.
  - Transaction rollback on database operation failures.

---

## Technologies Used

- **Language:** Python 3.x
- **Database:** MySQL
- **Connector:** MySQL Connector/Python (`mysql-connector-python`)
- **Configuration:** `python-dotenv`
- **Query Language:** SQL

---

## Project Structure

```text
employee-management-system/
│
├── employee_management.py     # Main application script
├── employee_management.sql    # Database schema creation script and sample data 
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variable template
├── .env                       # Local database credentials (not committed)
├── .gitignore                 # Files excluded from version control
└── README.md                  # Project documentation
```

> **Note:** The `.env` file contains sensitive local database credentials and is intentionally excluded from version control using `.gitignore`.

---

## Prerequisites

- Python 3.x
- MySQL Server
- MySQL Workbench or another MySQL client / CLI
- `pip` package manager

---

## Database Setup

Run the `employee_management.sql` script in your MySQL client to create the database, table, and sample employee records.

```sql
CREATE DATABASE IF NOT EXISTS employee_management_db;

USE employee_management_db;

CREATE TABLE IF NOT EXISTS employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender CHAR(1) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    department VARCHAR(100) NOT NULL,
    designation VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    joined_on DATE NOT NULL
);
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd employee-management-system
```

### 2. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
mysql-connector-python
python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
```

Replace `your_mysql_password` with your local MySQL password.

**Important:** Never commit the `.env` file to GitHub.

### 5. Run the Application

```bash
python employee_management.py
```

---

## Application Walkthrough

### Main Menu

```text
====Employee Management System====

1. View Employee Details
2. Insert Employee
3. Search Employee
4. Update Employee
5. Delete Employee
6. Analytics
7. Exit
```

### Analytics Menu

```text
1. Total Employees:
2. Department Statistics:
3. Average Salary Of Employees:
4. Maximum Salary Of Employees:
5. Minimum Salary Of Employees:
6. Department Average Salary:
7. Department -Wise Salary:
8. Gender Statistics:
9. Designation Statistics:
10. Salary Range Statistics:
11. Joining Year Statistics:
12. Department with Highest Average Salary:
13. Back
14. Exit
```

---

## Security

- Database credentials are stored in environment variables instead of being hard-coded into application files.
- The `.env` file is excluded from Git commits through `.gitignore`.
- SQL queries use parameter placeholders (`%s`) to help protect against SQL injection.
- Database operations use transaction handling with rollback on failures.

---

## Author

**Praneeth Reddy Katakam**

B.Tech – Computer Science and Engineering