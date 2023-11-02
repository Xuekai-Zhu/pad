def solution():
    video_game_spending_last_year = 100  # Ella spent $100 on video games last year
    total_money_last_year = video_game_spending_last_year / 0.4  # calculate Ella's total earnings last year
    raise_percentage = 0.1  # Ella received a 10% raise
    new_salary = (1 + raise_percentage) * total_money_last_year  # calculate Ella's new salary with the raise
    result = new_salary
    return result

print(solution())