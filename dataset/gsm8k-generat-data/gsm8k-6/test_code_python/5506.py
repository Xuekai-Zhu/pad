def solution():
    # Find the amount of water needed to fill the second tank completely
    second_tank_capacity = 450  # capacity of second tank
    second_tank_filled = 0.45 * second_tank_capacity  # amount of water in the second tank
    second_tank_empty = second_tank_capacity - second_tank_filled  # amount of space left in the second tank
    water_needed = second_tank_empty  # amount of water needed to fill the second tank completely

    # Find the additional amount of water needed to fill the first tank
    first_tank_capacity = 300  # capacity of first tank
    additional_water_needed = second_tank_capacity - first_tank_capacity

    # Find the total amount of water needed to fill both tanks
    total_water_needed = additional_water_needed + water_needed
    result = total_water_needed
    return result

print(solution())