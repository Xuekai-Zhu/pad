def solution():
    tire_capacity = 500
    flat_tires = 2
    tire1 = 0.4 * tire_capacity
    tire2 = 0.7 * tire_capacity

    # Calculate the total air needed to fill all tires
    total_air_needed = (2 * tire_capacity) - tire1 - tire2

    # Calculate the number of pumps needed to fill all tires
    pumps_needed = total_air_needed / 50
    result = pumps_needed
    return result

print(solution())