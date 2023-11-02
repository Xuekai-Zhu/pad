def solution():
    """A baker bakes 5 loaves of bread an hour in one oven. He has 4 ovens. From Monday to Friday, he bakes for 5 hours, but on Saturday and Sunday, he only bakes for 2 hours. How many loaves of bread does the baker bake in 3 weeks?"""
    loaves_per_hour = 5
    ovens = 4
    weekday_hours = 5
    weekend_hours = 2
    weekday_loaves = loaves_per_hour * ovens * weekday_hours
    weekend_loaves = loaves_per_hour * ovens * weekend_hours
    weekly_loaves = weekday_loaves * 5 + weekend_loaves * 2
    total_loaves = weekly_loaves * 3
    result = total_loaves
    return result

print(solution())