def solution():
    """Candy has a chair rental business. During the weekdays, 60 chairs are rented each day; but during weekends, 100 chairs are rented each day. If this continues, how many chairs in total will Candy be able to rent out in two 4-week months?"""
    chairs_weekday = 60
    chairs_weekend = 100
    weekdays_per_month = 20
    weekends_per_month = 8
    total_chairs = (chairs_weekday * weekdays_per_month * 2) + (chairs_weekend * weekends_per_month * 2)
    result = total_chairs
    return result

print(solution())