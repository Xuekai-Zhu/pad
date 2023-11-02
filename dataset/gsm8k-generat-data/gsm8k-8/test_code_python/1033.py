def solution():
    # Calculate how many calories James loses per hour dancing
    dance_calories_per_hour = 2 * 300

    # Calculate how many calories James loses per dance session
    dance_calories_per_session = dance_calories_per_hour * 0.5

    # Calculate how many calories James loses per day of dancing
    daily_dance_calories = dance_calories_per_session * 2

    # Calculate how many calories James loses per week of dancing
    weekly_dance_calories = daily_dance_calories * 4

    result = weekly_dance_calories
    return result

print(solution())