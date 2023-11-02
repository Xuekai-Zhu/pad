def solution():
    # Calculate the capacity of each tank
    tank_capacity = 450 / 0.45  # If 450 liters is 45% of the tank, then the capacity is 450 / 0.45

    # Calculate the amount of water needed to fill both tanks
    total_water_needed = 2 * tank_capacity - (300 + 450)  # Two tanks of equal capacity minus the amount already filled

    result = total_water_needed
    return result

print(solution())