def solution():
    tire_capacity = 500  # Each tire can hold 500 cubic inches of air
    flat_tires = 2  # Two of the tires are completely flat and empty
    tire_1 = 0.4 * tire_capacity  # Tire 1 is 40% full
    tire_2 = 0.7 * tire_capacity  # Tire 2 is 70% full

    # Calculate the total amount of air needed to fill all the tires
    total_air_needed = (4 * tire_capacity) - (flat_tires * tire_capacity + tire_1 + tire_2)

    # Calculate the number of pumps needed to fill all the tires
    num_pumps = total_air_needed / 50
    result = num_pumps
    return result

print(solution())