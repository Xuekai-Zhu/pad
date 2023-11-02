def solution():
    """Mike wants to be the best goalkeeper on his soccer team. He practices for 3 hours every weekday, on Saturdays he practices for 5 hours, and he takes Sundays off. How many hours will he practice from now until the next game, if his team has a game in 3 weeks?"""
    weekdays_practice = 3 * 5
    saturday_practice = 5
    off_days = 2  # Sunday and game day
    total_practice_hours = weekdays_practice + saturday_practice
    time_until_game = 3 * 7 - off_days  # 3 weeks times 7 days per week minus off days
    total_hours_until_game = time_until_game * total_practice_hours
    result = total_hours_until_game
    return result

print(solution())