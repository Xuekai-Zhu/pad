def solution():
    """Ralph watches TV for 4 hours a day from Monday to Friday, and 6 hours a day on Saturday and Sunday. How many hours does Ralph spend watching TV in one week?"""
    weekday_hours = 4 * 5
    weekend_hours = 6 * 2
    total_hours = weekday_hours + weekend_hours
    result = total_hours
    return result

print(solution())