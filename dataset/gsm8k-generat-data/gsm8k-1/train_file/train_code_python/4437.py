def solution():
    """The fall semester lasts 15 weeks. During the weekdays, Paris studies 3 hours a day for her classes. On the weekends, she spends 4 hours studying on Saturday and 5 hours studying on Sunday. How much time does Paris study during the semester?"""
    weeks = 15
    weekdays = 5
    weekenddays = 2
    weekday_hours = 3
    saturday_hours = 4
    sunday_hours = 5
    total_weekday_hours = weeks * weekdays * weekday_hours
    total_saturday_hours = weeks * weekenddays * saturday_hours
    total_sunday_hours = weeks * weekenddays * sunday_hours
    total_hours = total_weekday_hours + total_saturday_hours + total_sunday_hours
    result = total_hours
    return result

print(solution())