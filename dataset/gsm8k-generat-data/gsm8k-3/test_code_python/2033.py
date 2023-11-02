def solution():
    """In a town, there is a multi-story parking lot, which has room for 425 cars. The parking lot has 5 levels, each of the same size. How many more cars can one level fit if there are already 23 parked cars on that level?"""
    # Calculate the total number of cars that can fit in the parking lot
    total_cars = 425

    # Calculate the number of levels in the parking lot
    levels = 5

    # Calculate the maximum number of cars one level can fit
    max_cars_per_level = total_cars // levels

    # Calculate the number of cars parked on the level
    parked_cars = 23

    # Calculate the remaining number of cars the level can fit
    remaining_cars = max_cars_per_level - parked_cars

    # Display the remaining number of cars
    result = remaining_cars
    return result

print(solution())