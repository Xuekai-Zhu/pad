def solution():
    # Define the coffee bean usage for each time of day
    morning_usage = 3
    afternoon_usage = 3 * 3
    evening_usage = 3 * 2

    # Calculate the total coffee bean usage for one day
    daily_usage = morning_usage + afternoon_usage + evening_usage

    # Calculate the total coffee bean usage for one week
    weekly_usage = daily_usage * 7
    result = weekly_usage
    return result

print(solution())