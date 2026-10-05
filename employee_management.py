import mysql.connector
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 3306)),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor=connection.cursor()
def get_integer(prompt):
    while True:
        try:
            value=int(input(prompt))
            return value
        except ValueError:
            print("Invalid input Please enter a number")
def get_float(prompt):
    while True:
        try:
            value=float(input(prompt))
            return value
        except ValueError:
            print("Invalid input Please enter a number")
def get_date(prompt):
    while True:
        try:
            date=input(prompt)
            datetime.strptime(date,"%Y-%m-%d")
            return date
        except ValueError:
            print("invalid date!! Enter in the format YYYY-MM-DD")
def check_duplicate(column, value,empid=None):
    if column == "employee_id":
        query = "SELECT employee_id FROM employee WHERE employee_id=%s"
        cursor.execute(query, (value,))
        employee = cursor.fetchone()

        if employee:
            return True
        else:
            return False

    elif column == "email":
        if empid is None:
            query = "SELECT email FROM employee WHERE email=%s"
            cursor.execute(query, (value,))
        else:
            query = "SELECT email FROM employee WHERE email=%s and employee_id!=%s"
            cursor.execute(query, (value,empid))
        employee=cursor.fetchone()
        if employee:
            return True
        else:
            return False
def execute_update(query, values, stmt):
    try:
        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Employee {stmt} has been updated successfully!")
        else:
            print(f"No changes were made to {stmt}.")

    except mysql.connector.Error as err:
        connection.rollback()
        print("Error:", err)
def display_employee(employee):
    print("====================")
    print(" Employee Details")
    print("====================")
    print("Employee Id:",employee[0])
    print("Employee Name:",employee[1])
    print("Employee AGE:",employee[2])
    print("Employee Gender:",employee[3])
    print("Employee Phone Number:",employee[4])
    print("Employee Email:",employee[5])
    print("Employee Address:",employee[6])
    print("Employee Department:",employee[7])
    print("Employee Designation:",employee[8])
    print(f"Employee Salary:{employee[9]:.2f}")
    print("Employee joined on:",employee[10])
def view_employees():
    cursor.execute("SELECT * FROM employee")
    employees=cursor.fetchall()
    if employees:
        for emp in employees:
            display_employee(emp)
    else:
        print("No Employees Found")
def insert_employee():
    while True:
        empid=get_integer("Enter the id of Employee:")
        if check_duplicate("employee_id",empid):
            print("Employee Id already Exists")
        else:
            break
    empname=input("Enter the name of Employee:")
    while True:
        empage = get_integer("Enter age of the Employee: ")

        if 18 <= empage <= 100:
            break
        print("Invalid age. Please enter an age between 18 and 100.")
    while True:
        empgender=input("Enter the gender of Employee:").upper()
        if empgender in ("M","F"):
            break
        else:
            print("Enter only M or F")
    while True:
        empphone=input("Enter phone number of Employee:")
        if empphone.startswith("+"):
            if empphone[1:].isdigit() and len(empphone)==13:
                break
            else:
                print("Phone Number is Invalid")
        elif empphone.isdigit() and len(empphone)==10:
            break
        else:
            print("Phone Number is Invalid")
    while True:
        newemail=input("Enter email of the Employee:")
        if (
            newemail.count("@") == 1 and newemail.count(".")==1
            and newemail.index("@") > 0
            and newemail.index("@") < newemail.index(".")
            and newemail.index(".") < len(newemail) - 1
        ):
            if check_duplicate("email",newemail):
             print("These Email Already Exists!!")
            else:
                break
        else:
            print("Invalid Email!")
    empaddress=input("Enter the address of Employee:")
    empdepartment=input("Enter the department of Employee:")
    empdesignation=input("Enter the designation of Employee:")
    while True:
        newsalary=get_float("Enter the salary of the Employee:")
        if newsalary>0:
            break
        else:
            print("Check The salary Entered")
    empjoined=get_date("Enter the date Employee joined:")
    query="""INSERT INTO employee (
        employee_id,
        employee_name,
        age,
        gender,
        phone,
        email,
        address,
        department,
        designation,
        salary,
        joined_on
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values=(
        empid,
        empname,
        empage,
        empgender,
        empphone,
        newemail,
        empaddress,
        empdepartment,
        empdesignation,
        newsalary,
        empjoined
    )
    try:
        cursor.execute(query,values)
        connection.commit()
        print("inserted successfully!")
    except mysql.connector.Error as err:
        connection.rollback()
        print("Error:",err)
def search_employee():
    while True:
        option=get_integer("1.Search By ID\n 2.Search By Name\n 3.Exit\n")
        if option==1:
            searchid=get_integer("Enter The Employee id To Search:")    
            query="select*from employee where employee_id=%s"
            cursor.execute(query,(searchid,))
            employee=cursor.fetchone()
            if employee:
                display_employee(employee)
                break
            else:
                print("Employee not found!")
        elif option==2:
            searchname=input("Enter a name:")
            query="select * from employee where lower(employee_name) like lower(%s)"
            cursor.execute(query,(f"%{searchname}%",))
            employees=cursor.fetchall()
            if employees:
                for employee in employees:
                    display_employee(employee)
                break
            else:
                print("Employee Not found")
        elif option==3:
            break
        else:
            print("Invalid Choice!!")
def update_employee():
    while True:
        empid=get_integer("Enter Id Of The Employee To Update:")
        query="select * from employee where employee_id=%s"
        cursor.execute(query,(empid,))
        employee=cursor.fetchone()
        if employee:
            break
        print("Employee Not Found")
        
        choice = get_integer(
            "1. Enter another ID\n"
            "2. Exit\n"
            "Enter choice: ")
        if choice == 2:
            return

    while True:
        update=get_integer("Which One You Want To Update:\n"
                "1.Employee Name\n"
                "2.Employee Age\n"
                "3.Employee Gender\n"
                "4.Employee phone\n"
                "5.Employee email\n"
                "6.Employee Address\n"
                "7.Employee department\n"
                "8.Employee designation\n"
                "9.Employee salary\n"
                "10.Employee joining date\n"
                "11.EXIT\n"
                "Enter Your Choice:")
        if update==1:
            newname=input("Enter the New Name:")
            query="update employee set employee_name=%s where employee_id=%s"
            execute_update(query,(newname,empid),"Name")
        elif update==2:
            while True:
                newage = get_integer("Enter age of the Employee: ")
        
                if 18 <= newage <= 100:
                    break
                print("Invalid age. Please enter an age between 18 and 100.")
            query="update employee set age=%s where employee_id=%s"
            execute_update(query,(newage,empid),"AGE")
        elif update==3:
            while True:
                newgender=input("Enter the New gender of Employee:").upper()
                if newgender in ("M","F"):
                    break
                else:
                    print("Enter only M or F")
            query="update employee set Gender=%s where employee_id=%s"
            execute_update(query,(newgender,empid),"Gender")
        elif update==4:
            while True:
                newphone=input("Enter New phone number of Employee:")
                if newphone.startswith("+"):
                    if newphone[1:].isdigit() and len(newphone)==13:
                        break
                    else:
                        print("Phone Number is Invalid")
                elif newphone.isdigit() and len(newphone)==10:
                    break
                else:
                    print("Phone Number is Invalid")
            query="update employee set phone=%s where employee_id=%s"
            execute_update(query,(newphone,empid),"Phone")
        elif update==5:
            while True:
                    newemail=input("Enter New Email of the Employee:")
                    if (
                        newemail.count("@") == 1 and newemail.count(".")==1
                        and newemail.index("@") > 0
                        and newemail.index("@") < newemail.index(".")
                        and newemail.index(".") < len(newemail) - 1
                    ):
                        if check_duplicate("email",newemail,empid):
                         print("These Email Already Exists!!")
                        else:
                            break
                    else:
                        print("Invalid Email!")
            query="update employee set email=%s where employee_id=%s"
            execute_update(query,(newemail,empid),"Email")
        elif update==6:
            newaddress=input("Enter the New Address:")
            query="update employee set address=%s where employee_id=%s"
            execute_update(query,(newaddress,empid),"Address")
        elif update==7:
                newdept=input("Enter the New Department:")
                query="update employee set department=%s where employee_id=%s"
                execute_update(query,(newdept,empid),"Department")
        elif update==8:
                newdesignation=input("Enter the New Designation:")
                query="update employee set designation=%s where employee_id=%s"
                execute_update(query,(newdesignation,empid),"Designation")
        elif update==9:
                while True:
                        newsalary=get_float("Enter the New salary of the Employee:")
                        if newsalary>0:
                            break
                        else:
                            print("Check The salary Entered")
                query="update employee set salary=%s where employee_id=%s"
                execute_update(query,(newsalary,empid),"Salary")
        elif update==10:
                newdate=get_date("Enter the New Date:")
                query="update employee set joined_on=%s where employee_id=%s"
                execute_update(query,(newdate,empid),"Date")
        elif update==11:
            break
        else:
            print("CHECK YOUR CHOICE!")
def delete_employee():
    while True:
        empid = get_integer("Enter Employee ID: ")

        query = "select * from employee where employee_id=%s"
        cursor.execute(query, (empid,))
        employee = cursor.fetchone()

        if employee:
            display_employee(employee)

            while True:
                confir = get_integer(
                    "DO YOU WANT TO DELETE THIS RECORD?\n"
                    "1. YES\n"
                    "2. NO\n"
                    "Enter your choice: "
                )

                if confir == 1:
                    query = "delete from employee where employee_id=%s"

                    try:
                        cursor.execute(query, (empid,))
                        connection.commit()

                        if cursor.rowcount > 0:
                            print("DELETED SUCCESSFULLY!")
                            return

                    except mysql.connector.Error as err:
                        connection.rollback()
                        print("Error!", err)

                elif confir == 2:
                    return

                else:
                    print("Please Enter 1 or 2")

        else:
            print("Employee Not Found")
            return
def total_employee():
    query="select count(*) from employee"
    cursor.execute(query)
    employee=cursor.fetchone()
    print("Total Employees:",employee[0])
def department_stats():
    query='''select department,count(*)
    from employee group by department'''
    cursor.execute(query)
    stats=cursor.fetchall()
    if stats:
        print("="*40)
        print(f"{'Department':<25} {'Employee':<25}")
        print("="*40)
        for dept,count in stats:
            print(f"{dept:<25}{count:<25}")
        print("="*40)
    else:
        print("No Data Available!!")
def average_salary():
    query="select avg(salary) from employee"
    cursor.execute(query)
    avg=cursor.fetchone()
    if avg[0] is not None:
        print(f"Average:{avg[0]:.2f}")
    else:
        print("No Salary Data Available!!")
def max_salary():
    query="select max(salary) from employee"
    cursor.execute(query)
    maxi=cursor.fetchone()
    if maxi[0] is not None:
        print(f"maximum:{maxi[0]:.2f}")
    else:
        print("No Salary Data Available!!")
def min_salary():
    query="select min(salary) from employee"
    cursor.execute(query)
    mini=cursor.fetchone()
    if mini[0] is not None:
        print(f"minimum:{mini[0]:.2f}")
    else:
        print("No Salary Data Available!!")
def department_average_salary():
    query="""select department,avg(salary) from employee group by department """
    cursor.execute(query)
    sal=cursor.fetchall()
    if sal:
        print("="*40)
        print(f"{'Department':<25} {'Average':<25}")
        print("="*40)
        for dept,average in sal:
            print(f"{dept:<25}{average:<25.2f}")
        print("="*40)
    else:
        print("No Data Available!!")
def department_wise_salary():
    query="""select department,count(*),avg(salary) from employee group by department """
    cursor.execute(query)
    sal=cursor.fetchall()
    if sal:
        print("="*60)
        print(f"{'Department':<18} {'Employees':<15} {'Average Salary':<20}")
        print("="*60)
        for dept,count,average in sal:
            print(f"{dept:<18}{count:<15}{average:20.2f}")
        print("="*60)
    else:
        print("No Data Available!!")
def gender_stats():
    query="select gender,count(*) from employee group by gender"
    cursor.execute(query)
    stats=cursor.fetchall()
    if stats:
        print("="*40)
        print(f"{'Gender':<25}{'Employees':<25}")
        print("="*40)
        for gen,emp in stats:
            print(f"{gen:<25}{emp:<25}")
        print("="*40)
    else:
        print("No Data Available!!")
def designation_stats():
    query='''select designation,count(*)
    from employee group by designation'''
    cursor.execute(query)
    stats=cursor.fetchall()
    if stats:
        print("="*40)
        print(f"{'Designation':<25} {'Employee':<25}")
        print("="*40)
        for desi,count in stats:
            print(f"{desi:<25}{count:<25}")
        print("="*40)
    else:
        print("No Data Available!!")
def salary_range_stats():
    query='''
            select
                case 
                    when salary<30000 then 'Below 30000'
                    when salary between 30000 and 50000 then'30000-50000'
                    else 'above 50000'
                end as salary_range,
                count(*)
            from employee
            group by salary_range'''
    cursor.execute(query)
    stats=cursor.fetchall()
    if stats:
        print("="*40)
        print(f"{'Salary Range':<25} {'Employees':<25}")
        print("="*40)
        for salary_range,count in stats:
            print(f"{salary_range:<25}{count:<25}")
        print("="*40)
    else:
        print("No Data Available!!")
def joining_year_stats():
    query='''select year(joined_on),count(*) from employee
                group by year(joined_on)
                order by year(joined_on)'''
    cursor.execute(query)
    stats=cursor.fetchall()
    if stats:
        print("="*40)
        print(f"{'DATE':<25} {'Employees':<25}")
        print("="*40)
        for date,count in stats:
            print(f"{date:<25}{count:<25}")
        print("="*40)
    else:
        print("No Data Available!!")
def highest_average_salary_dept():
    query='''select department,avg(salary) from employee
                group by department
                order by avg(salary) desc
                limit 1'''
    cursor.execute(query)
    stats=cursor.fetchone()
    if stats:
        print("="*40)
        print(f"{'Department':<25} {'Average':<25}")
        print("="*40)
        if stats:
            dept,avg=stats
            print(f"{dept:<25}{avg:<25.2f}")
        else:
            print("No Employee Data Available!!")
        print("="*40)
    else:
        print("No Data Available!!")

def analytics_menu():
    while True:
        action=get_integer("1.Total Employees:\n"
                     "2.Department Statistics:\n"
                     "3.Average Salary Of Employees:\n"
                     "4.Maximum Salary Of  Employees:\n"
                     "5.Minimum Salary Of Employees:\n"
                     "6.Department Average Salary:\n"
                     "7.Department -Wise Salary:\n"
                     "8.Gender Statistics:\n"
                     "9.Designation Statistics:\n"
                     "10.Salary Range Statistics:\n"
                     "11.Joining Year Statistics:\n"
                     "12.Department with Highest Average Salary:\n"
                     "13.Back\n"
                     "14.Exit\n"
                     "Enter Your Choice:"
                     )
        if action==1:
            total_employee()
        elif action==2:
            department_stats()
        elif action==3:
            average_salary()
        elif action==4:
            max_salary()
        elif action==5:
            min_salary()
        elif action==6:
            department_average_salary()
        elif action==7:
            department_wise_salary()
        elif action==8:
            gender_stats()
        elif action==9:
            designation_stats()
        elif action==10:
            salary_range_stats()
        elif action==11:
            joining_year_stats()
        elif action==12:
            highest_average_salary_dept()
        elif action==13:
            return
        elif action==14:
            cursor.close()
            connection.close()  
            print("Thank You!!")
            exit()
        else:
            print("Invalid Choice!!")
        
while True:
    print("====Employee Management System====")
    action=get_integer("1.View Employee Details\n"
                "2.Insert Employee\n"
                "3.Search Employee\n"
                "4.Update Employee\n"
                "5.Delete Employee\n"
                "6.Analytics\n"
                "7.Exit\n"
                "Enter Your choice:")
    if action==1:
        view_employees()
    elif action==2:
        insert_employee()
    elif action==3:
        search_employee()
    elif action==4:
        update_employee()
    elif action==5:
        delete_employee()
    elif action==6:
        analytics_menu()
    elif action==7:
        print("Thank You!!")
        break
    else:
        print("invalid choice!")
cursor.close()
connection.close()