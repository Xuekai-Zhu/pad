def solution():
    """Ella spends 40% of the money she makes from babysitting on video games. Last year she spent $100. This year she received a 10% raise. What is Ella’s new salary?"""
    
    # Calculate Ella's salary last year
    video_game_spending_last_year = 100
    percent_of_salary_spent_on_video_games = 0.4
    salary_last_year = video_game_spending_last_year / percent_of_salary_spent_on_video_games
    
    # Calculate Ella's new salary after a 10% raise
    percent_raise = 0.1
    new_salary = salary_last_year * (1 + percent_raise)
    
    # Return the result
    result = new_salary
    return result

print(solution())