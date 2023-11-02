def solution():
    """There is very little car traffic on Happy Street. During the week, most cars pass it on Tuesday - 25. On Monday, 20% less than on Tuesday, and on Wednesday, 2 more cars than on Monday. On Thursday and Friday, it is about 10 cars each day. On the weekend, traffic drops to 5 cars per day. How many cars travel down Happy Street from Monday through Sunday?"""
    cars_on_tuesday = 25
    cars_on_monday = cars_on_tuesday * 0.8
    cars_on_wednesday = cars_on_monday + 2
    cars_on_thursday = 10
    cars_on_friday = 10
    cars_on_saturday = 5
    cars_on_sunday = 5
    total_cars = cars_on_tuesday + cars_on_monday + cars_on_wednesday + cars_on_thursday + cars_on_friday + cars_on_saturday + cars_on_sunday
    result = total_cars
    return result

print(solution())