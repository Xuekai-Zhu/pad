def solution():
    first_tank_capacity = 300
    second_tank_capacity = 450
    second_tank_percentage_filled = 0.45

    # Calculate the current volume of water in the second tank
    current_volume_second_tank = second_tank_capacity * second_tank_percentage_filled

    # Calculate the total volume of water in both tanks without filling the second tank completely
    total_volume_without_filling_second_tank = first_tank_capacity + current_volume_second_tank

    # Calculate the capacity of each tank
    tank_capacity = total_volume_without_filling_second_tank / 2

    # Calculate the amount of water needed to fill both tanks to their capacity
    water_needed = (tank_capacity - first_tank_capacity) + (tank_capacity - current_volume_second_tank)
    result = water_needed
    return result

print(solution())