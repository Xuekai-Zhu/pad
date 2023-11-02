def solution():
    day1_minutes = 2 * 60  # 2 hours of studying on day 1
    day2_minutes = 2 * day1_minutes  # double the amount of studying on day 2
    day3_minutes = (day2_minutes - 60)  # one hour less than day 2
    total_minutes = day1_minutes + day2_minutes + day3_minutes  # sum of minutes studied over 3 days
    result = total_minutes
    return result

print(solution())