def solution():
    """Jerome bought 5 new toy cars last month. This month he bought twice as many so that he has 40 toy cars now. How many toy cars did Jerome have originally?"""
    current_cars = 40
    last_month_cars = 5
    this_month_cars = (current_cars - last_month_cars) / 2
    original_cars = last_month_cars + this_month_cars
    result = original_cars
    return result

print(solution())