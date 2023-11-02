def solution():
    gas_mileage = 35  # estimated gas mileage of the car
    tank_capacity = 12  # capacity of the car's tank in gallons
    total_distance = 372  # total distance Pria drove

    # Calculate the actual mileage of the car
    actual_mileage = total_distance / tank_capacity

    # Calculate the difference between actual mileage and advertised mileage
    difference = gas_mileage - actual_mileage
    result = difference
    return result

print(solution())