def solution():
    cougar_sleep = 4   # sleep in hours
    zebra_sleep = cougar_sleep + 2   # sleep in hours
    days_in_week = 7
    hours_in_day = 24
    total_sleep_hours = (cougar_sleep + zebra_sleep) * days_in_week
    result = total_sleep_hours
    return result

print(solution())