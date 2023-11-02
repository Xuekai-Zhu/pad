def solution():
    """A baker bakes 5 loaves of bread an hour in one oven. He has 4 ovens. From Monday to Friday, he bakes for 5 hours, but on Saturday and Sunday, he only bakes for 2 hours. How many loaves of bread does the baker bake in 3 weeks?"""
    loaves_per_hour_per_oven = 5
    num_ovens = 4
    weekday_hours = 5
    weekend_hours = 2
    num_weekdays = 5
    num_weekends = 2
    total_hours_per_day = weekday_hours * num_weekdays + weekend_hours * num_weekends
    total_loaves_per_day = loaves_per_hour_per_oven * num_ovens * total_hours_per_day
    total_loaves_in_3_weeks = total_loaves_per_day * 21
    result = total_loaves_in_3_weeks
    return result

print(solution())