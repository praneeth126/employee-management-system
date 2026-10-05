CREATE DATABASE IF NOT EXISTS employee_management_db;

USE employee_management_db;

CREATE TABLE IF NOT EXISTS employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(1) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    address VARCHAR(255),
    department VARCHAR(100),
    designation VARCHAR(100),
    salary DECIMAL(12,2) NOT NULL,
    joined_on DATE NOT NULL
);

INSERT INTO employee
(employee_id, employee_name, age, gender, phone, email, address, department, designation, salary, joined_on)
VALUES
(1001, 'Rahul Sharma', 28, 'M', '9876543210', 'rahul.sharma@example.com',
 'Bengaluru, Karnataka', 'IT', 'Software Developer', 55000.00, '2023-06-15'),

(1002, 'Priya Reddy', 26, 'F', '9876543211', 'priya.reddy@example.com',
 'Hyderabad, Telangana', 'HR', 'HR Executive', 42000.00, '2024-01-10'),

(1003, 'Arjun Kumar', 31, 'M', '9876543212', 'arjun.kumar@example.com',
 'Chennai, Tamil Nadu', 'Finance', 'Financial Analyst', 62000.00, '2022-08-22'),

(1004, 'Sneha Patel', 29, 'F', '9876543213', 'sneha.patel@example.com',
 'Mumbai, Maharashtra', 'Marketing', 'Marketing Executive', 48000.00, '2023-03-18'),

(1005, 'Vikram Singh', 35, 'M', '9876543214', 'vikram.singh@example.com',
 'Delhi, India', 'IT', 'Senior Software Developer', 85000.00, '2021-11-05'),

(1006, 'Ananya Rao', 24, 'F', '9876543215', 'ananya.rao@example.com',
 'Pune, Maharashtra', 'Operations', 'Operations Executive', 38000.00, '2024-07-12'),

(1007, 'Karthik Reddy', 30, 'M', '9876543216', 'karthik.reddy@example.com',
 'Hyderabad, Telangana', 'IT', 'Database Administrator', 70000.00, '2022-05-30'),

(1008, 'Meera Nair', 27, 'F', '9876543217', 'meera.nair@example.com',
 'Kochi, Kerala', 'Finance', 'Accountant', 45000.00, '2023-09-14'),

(1009, 'Aditya Verma', 33, 'M', '9876543218', 'aditya.verma@example.com',
 'Jaipur, Rajasthan', 'Sales', 'Sales Manager', 68000.00, '2021-04-20'),

(1010, 'Divya Krishnan', 25, 'F', '9876543219', 'divya.krishnan@example.com',
 'Bengaluru, Karnataka', 'Marketing', 'Marketing Analyst', 52000.00, '2024-02-26');