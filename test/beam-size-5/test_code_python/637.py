def solution():
    
    # Define Tim's salary and the percentage raise
    salary = 20000
    raise_percentage = 0.05

    # Calculate Tim's salary after a 5% raise
    salary_after_raise = salary * (1 + raise_percentage)

    # Calculate Tim's salary after a bonus
    salary_after_bonus = salary_after_raise / 2

    # Calculate Tim's salary after a year
    salary_after_year = salary_after_raise + salary_after_bonus

    # Display Tim's salary after a year
    result = salary_after_year
    return result

print(solution())