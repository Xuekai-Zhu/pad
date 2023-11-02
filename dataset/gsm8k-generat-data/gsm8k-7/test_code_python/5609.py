def solution():
    hours_per_day = 4
    num_days = 14
    completion_percentage = 0.4
    new_hours_per_day = 7

    # Calculate the total hours John played in two weeks
    total_hours_played = hours_per_day * num_days

    # Calculate the total hours required to finish the game
    total_hours_required = total_hours_played / completion_percentage

    # Calculate the remaining hours needed to finish the game after increasing playtime
    remaining_hours = total_hours_required - (num_days * hours_per_day)

    # Calculate the number of days needed to finish the game with increased playtime
    days_needed = remaining_hours / new_hours_per_day
    result = days_needed
    return result

print(solution())