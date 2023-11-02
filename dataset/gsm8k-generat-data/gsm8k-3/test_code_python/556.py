def solution():
    """Roberto recently received a 20% raise from his previous salary, which was already 40% higher than his starting salary. If Roberto's starting salary was $80,000, what is his current salary?"""
    # Define Roberto's starting salary
    start_salary = 80000

    # Calculate Roberto's second salary after a 40% increase
    second_salary = start_salary * 1.4

    # Calculate Roberto's current salary after a 20% raise
    current_salary = second_salary * 1.2

    # Display Roberto's current salary
    result = current_salary
    return result

print(solution())