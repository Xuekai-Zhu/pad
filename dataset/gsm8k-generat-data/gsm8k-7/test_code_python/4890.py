def solution():
    starting_mileage = 1728
    gas_tank_capacity = 20
    mpg = 30

    # Calculate the total distance Marcus' car covered on the trip
    total_distance = (gas_tank_capacity * mpg) * 2

    # Add the total distance to the starting mileage to get the current mileage
    current_mileage = starting_mileage + total_distance
    result = current_mileage
    return result

print(solution())