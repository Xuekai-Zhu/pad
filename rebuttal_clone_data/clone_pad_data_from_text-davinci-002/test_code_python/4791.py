def solution():
    cougar_hours = 4
    zebra_hours = 2
    hours_per_day = 24
    days_per_week = 7
    cougar_sleep = cougar_hours * hours_per_day * days_per_week
    zebra_sleep = zebra_hours * hours_per_day * days_per_week
    total_sleep = cougar_sleep + zebra_sleep
    result = total_sleep
    return result

print(solution())