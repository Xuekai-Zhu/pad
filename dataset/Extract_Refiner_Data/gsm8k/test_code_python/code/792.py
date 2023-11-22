def solution():
    
    # Define the initial employee number and the number of employees hired per month
    initial_employee = 200
    employees_per_month = 20

    # Define the salary per employee and the number of months
    salary_per_employee = 4000
    months = 3

    # Calculate the total number of employees hired after three months
    total_employees = employees_per_month * months

    # Calculate the total amount paid to employees after three months
    total_salary = total_employees * salary_per_employee

    # Display the total salary paid
    result = total_salary
    return result

print(solution())