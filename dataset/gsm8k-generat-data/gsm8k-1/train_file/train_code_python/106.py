def solution():
    """There is very little car traffic on Happy Street. During the week, most cars pass it on Tuesday - 25. On Monday, 20% less than on Tuesday, and on Wednesday, 2 more cars than on Monday. On Thursday and Friday, it is about 10 cars each day. On the weekend, traffic drops to 5 cars per day. How many cars travel down Happy Street from Monday through Sunday?"""
    tuesday = 25
    monday = tuesday * 0.8
    wednesday = monday + 2
    thursday = 10
    friday = 10
    weekend = 5 * 2
    total_cars = tuesday + monday + wednesday + thursday + friday + weekend
    result = total_cars
    return result

print(solution())