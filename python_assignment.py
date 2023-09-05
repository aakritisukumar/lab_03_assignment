print("Aakriti")
print("E22CSEU0863")


class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000),
]

def by_age(employees, operator, value):
    results = []
    for employee in employees:
        if operator == '>' and employee.age > value:
            results.append(employee)
        elif operator == '<' and employee.age < value:
            results.append(employee)
        elif operator == '>=' and employee.age >= value:
            results.append(employee)
        elif operator == '<=' and employee.age <= value:
            results.append(employee)
    return results

def by_salary(employees, operator, value):
    results = []
    for employee in employees:
        if operator == '>' and employee.salary > value:
            results.append(employee)
        elif operator == '<' and employee.salary < value:
            results.append(employee)
        elif operator == '>=' and employee.salary >= value:
            results.append(employee)
        elif operator == '<=' and employee.salary <= value:
            results.append(employee)
    return results

def by_emp_id(employees, emp_id):
    results = []
    for employee in employees:
        if employee.emp_id == emp_id:
            results.append(employee)
    return results

def main():
    while True:
        print("\nMenu:")
        print("1. Search by Age")
        print("2. Search by Salary")
        print("3. Search by Employee ID")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            operator = input("Enter operator (> < >= <=): ")
            value = int(input("Enter age value: "))
            results = by_age(employees, operator, value)
        elif choice == '2':
            operator = input("Enter operator (> < >= <=): ")
            value = float(input("Enter salary value: "))
            results = by_salary(employees, operator, value)
        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            results = by_emp_id(employees, emp_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if not results:
            print("No matching records found.")
        else:
            print("\nMatching Employees:")
            for employee in results:
                print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

if __name__ == "__main__":
    main()
