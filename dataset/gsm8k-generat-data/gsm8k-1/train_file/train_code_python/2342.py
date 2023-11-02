def solution():
    """Jerome bought 5 new toy cars last month. This month he bought twice as many so that he has 40 toy cars now. How many toy cars did Jerome have originally?"""
    new_cars_this_month = 2 * 5
    total_cars = 40
    original_cars = total_cars - new_cars_this_month
    result = original_cars
    return result

print(solution())