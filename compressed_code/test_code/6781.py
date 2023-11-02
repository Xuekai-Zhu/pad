def solution():
    
    current_salary = 500
    raise_percent = 6
    raise_amount = current_salary * (raise_percent / 100)
    new_salary = current_salary + raise_amount
    result = new_salary
    return result

print(solution())