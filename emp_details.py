# employee_details.py

# Accept employee details
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
post = input("Enter Employee Post: ")
salary = float(input("Enter Employee Salary: "))

# Display employee details
print("\n------ EMPLOYEE DETAILS ------")
print("Employee ID   :", emp_id)
print("Name          :", name)
print("Post          :", post)
print("Salary        :", salary)

# Salary category
if salary >= 50000:
    print("Category      : High Salary")
elif salary >= 30000:
    print("Category      : Medium Salary")
else:
    print("Category      : Low Salary")
