def solution():
    # Calculate the total number of cars parked in the parking lot
    parked_cars = 23 * 5  # there are five levels in total

    # Calculate the number of cars that can still be parked on one level
    remaining_cars = 425 - parked_cars
    cars_per_level = remaining_cars // 5   # divide by 5 since there are 5 levels of the same size

    # Calculate the number of additional cars that can fit on one level
    additional_cars = cars_per_level - 23
    result = additional_cars
    return result

print(solution())