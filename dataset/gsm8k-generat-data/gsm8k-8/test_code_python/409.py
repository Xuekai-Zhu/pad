def solution():
    # Calculate total cars sold in the first 7 days
    total_cars_first_week = 5*3 + 3*4

    # Calculate remaining days in the month
    remaining_days = 30 - 7

    # Calculate average cars needed to meet quota per day
    cars_per_day = (50 - total_cars_first_week) / remaining_days

    # Calculate cars needed to be sold for remaining days
    remaining_cars = cars_per_day * remaining_days
    result = remaining_cars
    return result

print(solution())