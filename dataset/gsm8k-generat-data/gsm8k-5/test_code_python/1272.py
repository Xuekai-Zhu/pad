def solution():
    current_salary = 500  # Ruiz's current monthly salary is $500
    raise_percentage = 6  # Ruiz received a 6% raise
    raise_amount = current_salary * (raise_percentage / 100)  # Calculate the raise amount
    new_salary = current_salary + raise_amount  # Calculate Ruiz's new salary

    result = new_salary
    return result

print(solution())