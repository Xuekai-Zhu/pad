def solution():
    """Summer performs 5 sun salutation yoga poses as soon as she gets out of bed, on the weekdays. How many sun salutations will she perform throughout an entire year?"""
    sun_salutations_per_day = 5
    days_per_week = 5
    weeks_per_year = 52
    total_sun_salutations = sun_salutations_per_day * days_per_week * weeks_per_year
    result = total_sun_salutations
    return result

print(solution())