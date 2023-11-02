def solution():
    previous_salary = 80000
    raise_percentage = 20
    new_salary = previous_salary * (1 + (raise_percentage / 100))
    current_salary = new_salary * (1 + (40 / 100))
    result = current_salary
    return result

print(solution())