def solution():
    """Mike wants to be the best goalkeeper on his soccer team. He practices for 3 hours every weekday, on Saturdays he practices for 5 hours, and he takes Sundays off. How many hours will he practice from now until the next game, if his team has a game in 3 weeks?"""
    weekdays = 5
    weekday_hours = 3
    saturday_hours = 5
    off_days = 1
    weeks_until_game = 3
    total_weekday_hours = weekdays * weekday_hours * weeks_until_game
    total_saturday_hours = saturday_hours * weeks_until_game
    total_off_days = off_days * weeks_until_game
    total_hours = total_weekday_hours + total_saturday_hours

    return total_hours

print(solution())