def solution():
    days_with_3_hours = 2
    days_with_60_percent_sleep = 7 - days_with_3_hours
    total_sleep = days_with_3_hours * 3 + days_with_60_percent_sleep * 0.6 * 8
    result = total_sleep
    return result

print(solution())