def solution():
    initial_salary = 10000
    percent_increase = 2
    increase_amount = initial_salary * (percent_increase / 100)
    new_salary = initial_salary + increase_amount
    result = new_salary
    return result

print(solution())