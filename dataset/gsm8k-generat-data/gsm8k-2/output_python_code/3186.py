def solution():
    """Summer performs 5 sun salutation yoga poses as soon as she gets out of bed, on the weekdays. How many sun salutations will she perform throughout an entire year?"""
    sun_salutations_per_day = 5
    weekdays_in_year = 260 # assuming 5-day workweek, 52 weeks in a year
    total_salutations = sun_salutations_per_day * weekdays_in_year
    result = total_salutations
    return result

print(solution())