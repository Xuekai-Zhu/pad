def solution():
    """Roberto recently received a 20% raise from his previous salary, which was already 40% higher than his starting salary. If Roberto's starting salary was $80,000, what is his current salary?"""
    starting_salary = 80000
    prev_salary = starting_salary * 1.4
    new_salary = prev_salary * 1.2
    result = new_salary
    return result

print(solution())