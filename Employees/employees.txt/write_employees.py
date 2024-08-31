def write_employee_details(file_path, employees):
    """Write employee details to a file.

    Args:
        file_path (str): Path to the file to write to.
        employees (list of dict): List of employee details where each employee is represented by a dictionary.
    """
    try:
        with open(file_path, 'w') as file:
            for employee in employees:
                name = employee.get('name', 'N/A')
                age = employee.get('age', 'N/A')
                salary = employee.get('salary', 'N/A')
                file.write(f"Name: {name}, Age: {age}, Salary: {salary}\n")
        print(f"Employee details written to {file_path} successfully.")
    except IOError as e:
        print(f"An error occurred: {e}")

# Define employee details
employees = [
    {'name': 'Alice Johnson', 'age': 30, 'salary': 70000},
    {'name': 'Bob Smith', 'age': 45, 'salary': 85000},
    {'name': 'Charlie Brown', 'age': 28, 'salary': 60000}
]

# File path
file_path = 'employees.txt'

# Write employee details to the filepython write_employees.py

write_employee_details(file_path, employees)
