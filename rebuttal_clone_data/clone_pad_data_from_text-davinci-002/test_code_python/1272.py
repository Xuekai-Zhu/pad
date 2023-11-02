def solution():
    salary = 500
    percent_raise = 6
    raise_amount = salary * (percent_raise / 100)
    new_salary = raise_amount + salary
    result = new_salary
    return result

print(solution())