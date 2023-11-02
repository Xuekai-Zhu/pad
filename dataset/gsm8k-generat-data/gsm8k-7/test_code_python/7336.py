def solution():
    miles_per_day = 5
    weekdays_per_week = 5
    weeks = 3

    # Calculate the total number of weekdays over three weeks
    total_weekdays = weeks * weekdays_per_week

    # Calculate the total number of miles Damien runs
    total_miles = total_weekdays * miles_per_day
    result = total_miles
    return result

print(solution())