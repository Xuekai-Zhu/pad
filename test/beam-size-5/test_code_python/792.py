def solution():
    
    # Define the initial employee number and the salary per month
    initial_employee = 200
    salary_per_month = 4000

    # Calculate the total number of employees after three months
    total_employees = initial_employee + (20 * salary_per_month)

    # Calculate the total amount of money the company pays to its employees after three months
    total_salary = total_employees * salary_per_month

    # return the result
    result = total_salary
    return result

print(solution())