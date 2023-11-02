def solution():
    """Ella spends 40% of the money she makes from babysitting on video games. Last year she spent $100. This year she received a 10% raise. What is Ella’s new salary?"""
    # Define Ella's video game spending as a percentage of her salary and the amount spent last year
    video_game_spending_percentage = 0.4
    last_year_spending = 100

    # Calculate Ella's salary from her video game spending last year
    total_salary_last_year = last_year_spending / video_game_spending_percentage

    # Calculate Ella's new salary with a 10% raise
    new_salary = total_salary_last_year * 1.1

    # return the result
    result = new_salary
    return result

print(solution())