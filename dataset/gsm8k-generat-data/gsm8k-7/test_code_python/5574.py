def solution():
    weekdays_practice = 3  # hours
    saturdays_practice = 5  # hours
    days_until_game = 3 * 7  # 3 weeks
    total_weekdays = 5

    # Calculate the total number of weekday hours
    weekday_hours = weekdays_practice * total_weekdays * days_until_game

    # Calculate the total number of Saturday hours
    saturday_hours = saturdays_practice * (days_until_game // 7)

    # Calculate the total number of hours
    total_hours = weekday_hours + saturday_hours
    result = total_hours
    return result

print(solution())