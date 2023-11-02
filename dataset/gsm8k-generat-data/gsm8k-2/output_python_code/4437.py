def solution():
    """The fall semester lasts 15 weeks. During the weekdays, Paris studies 3 hours a day for her classes.
    On the weekends, she spends 4 hours studying on Saturday and 5 hours studying on Sunday. How much time does Paris study during the semester?"""
    weekdays = 5  # days per week
    weekday_hours = 3  # hours per weekday
    weekend_hours = 9  # hours per weekend day
    total_weekdays = weekdays * 15  # number of weekdays in the semester
    total_weekends = 2 * 15  # number of weekends in the semester
    total_hours = (total_weekdays * weekday_hours) + (total_weekends * weekend_hours)
    result = total_hours
    return result

print(solution())