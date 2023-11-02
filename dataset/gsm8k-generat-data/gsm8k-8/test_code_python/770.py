def solution():
    # Calculate the total number of days in 2 weeks
    total_days = 2 * 7

    # Calculate the total number of days the children are allowed to watch TV
    days_watching_tv = 4 * total_days / 7

    # Calculate the total time spent watching TV
    total_time = days_watching_tv * 45 / 60

    result = total_time
    return result

print(solution())