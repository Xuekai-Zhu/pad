def solution():
    salary = 500
    raise_percentage = 0.06

    raise_amount = salary * raise_percentage
    new_salary = salary + raise_amount
    result = new_salary
    return result

print(solution())