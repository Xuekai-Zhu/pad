def solution():
    """Roberto recently received a 20% raise from his previous salary, which was already 40% higher than his starting salary. If Roberto's starting salary was $80,000, what is his current salary?"""
    starting_salary = 80000
    previous_salary = starting_salary * (1 + 0.4)
    current_salary = previous_salary * (1 + 0.2)
    result = current_salary
    return result

print(solution())