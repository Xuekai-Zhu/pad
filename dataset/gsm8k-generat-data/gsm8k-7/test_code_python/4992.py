def solution():
    estimated_mileage = 35
    tank_size = 12
    total_miles_driven = 372

    # Calculate the actual mileage of the car
    actual_mileage = total_miles_driven / tank_size

    # Calculate the difference between actual and estimated mileage
    difference = estimated_mileage - actual_mileage
    result = difference
    return result

print(solution())