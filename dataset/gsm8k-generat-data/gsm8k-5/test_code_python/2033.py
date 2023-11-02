def solution():
    total_cars = 425  # The parking lot has room for 425 cars
    levels = 5  # The parking lot has 5 levels
    occupied_cars = 23  # There are already 23 parked cars on one level

    # Calculate how many cars can fit on one level
    cars_per_level = total_cars / levels

    # Calculate how many more cars can fit on one level
    remaining_cars = cars_per_level - occupied_cars
    result = remaining_cars
    return result

print(solution())