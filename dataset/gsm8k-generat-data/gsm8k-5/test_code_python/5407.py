def solution():
    # Calculate the total time Jill spent studying each day
    day1 = 2 * 60  # 2 hours of studying on day 1 = 120 minutes
    day2 = 4 * 60  # Double the amount of studying on day 2 = 240 minutes
    day3 = (4 * 60) - 60  # One hour less than day 2 on day 3 = 180 minutes

    # Calculate the total time Jill spent studying over the 3 days
    total_time = day1 + day2 + day3
    result = total_time
    return result

print(solution())