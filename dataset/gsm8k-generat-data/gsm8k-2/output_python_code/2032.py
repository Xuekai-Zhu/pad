def solution():
    """In a town, there is a multi-story parking lot which has room for 425 cars. The parking lot has 5 levels, each of the same size. How many more cars can one level fit if there are already 23 parked cars on that level?"""
    total_cars = 425
    num_levels = 5
    total_parked_cars = 23*num_levels
    remaining_cars = total_cars - total_parked_cars
    cars_per_level = remaining_cars / num_levels
    extra_cars = cars_per_level - 23
    result = extra_cars
    return result

print(solution())