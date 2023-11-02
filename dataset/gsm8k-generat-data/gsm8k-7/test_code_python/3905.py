def solution():
    laps_per_day = 12
    days_per_week = 5
    weeks = 5

    # Calculate the total number of laps Jasmine swims in one week
    weekly_laps = laps_per_day * days_per_week

    # Calculate the total number of laps Jasmine swims in five weeks
    total_laps = weekly_laps * weeks
    result = total_laps
    return result

print(solution())