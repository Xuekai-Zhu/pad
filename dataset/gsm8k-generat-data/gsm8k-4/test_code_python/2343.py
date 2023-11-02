def solution():
    """Jerome bought 5 new toy cars last month. This month he bought twice as many so that he has 40 toy cars now. How many toy cars did Jerome have originally?"""
    # Define the number of toy cars bought last month
    last_month_cars = 5

    # Define the current total number of toy cars
    current_total_cars = 40

    # Calculate the number of toy cars bought this month
    this_month_cars = current_total_cars - last_month_cars

    # Calculate the number of toy cars Jerome had originally
    original_cars = (last_month_cars + this_month_cars) / 2

    result = original_cars
    return result

print(solution())