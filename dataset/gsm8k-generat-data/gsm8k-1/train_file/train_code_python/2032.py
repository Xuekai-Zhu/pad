def solution():
    """In a town, there is a multi-story parking lot, which has room for 425 cars. The parking lot has 5 levels, each of the same size. How many more cars can one level fit if there are already 23 parked cars on that level?"""
    total_capacity = 425
    number_of_levels = 5
    cars_already_parked = 23
    cars_per_level = (total_capacity - cars_already_parked) / number_of_levels
    result = cars_per_level
    return result

print(solution())