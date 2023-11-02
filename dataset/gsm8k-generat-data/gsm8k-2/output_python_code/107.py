def solution():
    """There is very little car traffic on Happy Street. During the week, most cars pass it on Tuesday - 25. On Monday, 20% less than on Tuesday, and on Wednesday, 2 more cars than on Monday. On Thursday and Friday, it is about 10 cars each day. On the weekend, traffic drops to 5 cars per day. How many cars travel down Happy Street from Monday through Sunday?"""
    tuesday_cars = 25
    monday_cars = 0.8 * tuesday_cars
    wednesday_cars = monday_cars + 2
    thursday_cars = 10
    friday_cars = 10
    weekend_cars = 5 * 2
    total_cars = tuesday_cars + monday_cars + wednesday_cars + thursday_cars + friday_cars + weekend_cars
    result = total_cars
    return result

print(solution())