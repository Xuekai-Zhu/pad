def solution():
    # Calculate the total number of practice hours until the next game
    weekdays = 5  # number of weekdays in a week
    saturdays = 1  # number of Saturdays in a week
    total_practice_days = 3 * weekdays + 5 * saturdays  # total number of practice days in a week
    total_practice_hours = total_practice_days * 3  # number of practice hours in a day
    total_practice_hours_until_game = total_practice_hours * 3  # number of practice hours in 3 weeks (assuming the game is in 3 weeks)
    result = total_practice_hours_until_game
    return result

print(solution())