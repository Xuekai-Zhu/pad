def solution():
    # Calculate the total number of cars that can be parked on one level
    total_cars_on_one_level = 425 / 5

    # Subtract the number of parked cars from the total to get the remaining capacity
    remaining_capacity = total_cars_on_one_level - 23

    result = remaining_capacity
    return result

print(solution())