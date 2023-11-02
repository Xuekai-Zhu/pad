def solution():
    """Roberto recently received a 20% raise from his previous salary, which was already 40% higher than his starting salary. If Roberto's starting salary was $80,000, what is his current salary?"""
    # Define Roberto's starting salary
    starting_salary = 80000

    # Calculate Roberto's salary after 40% raise
    after_40_raise = starting_salary * 1.4

    # Calculate Roberto's salary after 20% raise from the previous salary
    current_salary = after_40_raise * 1.2

    result = current_salary
    return result

print(solution())