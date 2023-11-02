def solution():
    # Calculate the total TV watching time in one week
    weekly_TV_time = 5 * 0.5 + 2  # 5 weekdays with 30 minutes per day, 2 extra hours on the weekends
    total_TV_time = weekly_TV_time * 52  # multiply by 52 weeks in a year
    result = total_TV_time
    return result

print(solution())