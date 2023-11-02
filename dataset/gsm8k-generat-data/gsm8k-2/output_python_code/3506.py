def solution():
    """Ella spends 40% of the money she makes from babysitting on video games. Last year she spent $100. This year she received a 10% raise. What is Ella’s new salary?"""
    video_game_spending = 100
    percent_spending = 0.4
    total_salary = (video_game_spending * 100) / percent_spending
    new_salary = total_salary * 1.1
    result = new_salary
    return result

print(solution())