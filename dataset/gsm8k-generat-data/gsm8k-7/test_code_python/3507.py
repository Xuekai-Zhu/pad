def solution():
    money_spent_on_games_last_year = 100
    percentage_of_salary_spent_on_games = 0.4

    # Calculate Ella's salary last year
    salary_last_year = money_spent_on_games_last_year / percentage_of_salary_spent_on_games

    # Calculate Ella's new salary with the 10% raise
    new_salary = salary_last_year * 1.1
    result = new_salary
    return result

print(solution())