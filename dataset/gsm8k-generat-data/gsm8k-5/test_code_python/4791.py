def solution():
    cougar_sleep = 4  # hours of sleep per night for the cougar
    zebra_sleep = cougar_sleep + 2  # hours of sleep per night for the zebra
    days_per_week = 7  # number of days in a week

    # Calculate total hours of sleep for the cougar and zebra in a week
    total_sleep_hours = (cougar_sleep + zebra_sleep) * days_per_week

    result = total_sleep_hours
    return result

print(solution())