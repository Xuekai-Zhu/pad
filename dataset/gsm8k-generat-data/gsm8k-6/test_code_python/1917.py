def solution():
    # Calculate the new salary after a 2% increase
    current_salary = 10000
    increase_percentage = 2/100
    salary_increase = current_salary * increase_percentage
    new_salary = current_salary + salary_increase
    result = new_salary
    return result

print(solution())