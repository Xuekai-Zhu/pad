def solution():
    cans_per_30_min = 30
    minutes_per_hour = 60
    hours = 8

    # Calculate the total number of 30-minute intervals in 8 hours
    intervals = hours * (minutes_per_hour / 30)

    # Calculate the total number of cans produced
    total_cans = intervals * cans_per_30_min
    result = total_cans
    return result

print(solution())