# emp_details.py

def salary_category(salary):
    if salary >= 50000:
        return "High Salary"
    elif salary >= 30000:
        return "Medium Salary"
    else:
        return "Low Salary"


def main():
    print("=== Employee Management System ===")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    post = input("Enter Employee Post: ")

    try:
        salary = float(input("Enter Employee Salary: "))
    except ValueError:
        print("Invalid salary! Please enter numbers only.")
        return

    category = salary_category(salary)

    print("\n----- Employee Report -----")
    print(f"Employee ID : {emp_id}")
    print(f"Name        : {name}")
    print(f"Post        : {post}")
    print(f"Salary      : {salary}")
    print(f"Category    : {category}")
    print("---------------------------")


if __name__ == "__main__":
    main()
