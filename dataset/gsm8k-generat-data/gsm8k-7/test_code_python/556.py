def solution():
    starting_salary = 80000
    previous_salary = starting_salary * 1.4  # 40% higher than starting salary
    raise_percent = 0.2  # 20% raise
    current_salary = previous_salary * (1 + raise_percent)
    result = current_salary
    return result

print(solution())