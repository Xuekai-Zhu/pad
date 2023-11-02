def solution():
    percent_spent = 40
    initial_salary = 100
    raise_percent = 10
    raise_amount = initial_salary * (raise_percent / 100)
    new_salary = initial_salary + raise_amount
    new_spent = new_salary * (percent_spent / 100)
    result = new_spent
    return result

print(solution())