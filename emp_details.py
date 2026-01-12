def get_employee(emp_id, name, post, salary):
    print("\n------ EMPLOYEE DETAILS ------")
    print("Employee ID   :", emp_id)
    print("Name          :", name)
    print("Post          :", post)
    print("Salary        :", salary)

    if salary >= 50000:
        return "High Salary"
    elif salary >= 30000:
        return "Medium Salary"
    else:
        return "Low Salary"


if __name__ == "__main__":
    # Jenkins-safe hardcoded values
    emp_id = "101"
    name = "Ravi"
    post = "Manager"
    salary = 60000

    category = get_employee(emp_id, name, post, salary)
    print("Category      :", category)
