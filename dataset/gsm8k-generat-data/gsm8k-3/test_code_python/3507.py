def solution():
    """Ella spends 40% of the money she makes from babysitting on video games. Last year she spent $100. This year she received a 10% raise. What is Ella’s new salary?"""
    # Define the percentage of earnings Ella spends on video games
    VIDEO_GAME_PERCENTAGE = 0.4

    # Define last year's spending on video games
    last_year_spending = 100

    # Calculate Ella's earnings last year
    last_year_earnings = last_year_spending / (1 - VIDEO_GAME_PERCENTAGE)

    # Calculate Ella's new salary after a 10% raise
    new_salary = last_year_earnings * 1.1

    # Display Ella's new salary
    result = new_salary
    return result

print(solution())