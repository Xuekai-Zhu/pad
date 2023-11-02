def solution():
    initial_sun_set = 6 * 60  # convert 6 PM to minutes
    minutes_added_per_day = 1.2
    days_since_march_1st = 40

    # Calculate the total number of minutes that the sun sets later than March 1st
    total_minutes_added = minutes_added_per_day * days_since_march_1st

    # Calculate the current time in minutes
    current_time = 6 * 60 + 10  # convert 6:10 PM to minutes

    # Calculate the time of the current sunset
    current_sun_set = initial_sun_set + total_minutes_added

    # Calculate the number of minutes until the current sunset
    minutes_until_sun_set = current_sun_set - current_time
    result = minutes_until_sun_set
    return result

print(solution())