def solution():
    # Calculate Ella's previous salary
    previous_spending = 100  # Ella spent $100 on video games last year
    spending_percentage = 0.4  # Ella spends 40% of her salary on video games
    previous_salary = previous_spending / spending_percentage

    # Calculate Ella's new salary after a 10% raise
    raise_percentage = 0.1
    new_salary = previous_salary * (1 + raise_percentage)

    result = new_salary
    return result

print(solution())