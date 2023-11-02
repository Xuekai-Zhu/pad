def solution():
    # Define the capacities of the three tanks
    tank1_capacity = 7000
    tank2_capacity = 5000
    tank3_capacity = 3000

    # Calculate how much water is in each tank
    tank1_water = 0.75 * tank1_capacity
    tank2_water = 0.8 * tank2_capacity
    tank3_water = 0.5 * tank3_capacity

    # Calculate the total amount of water in all three tanks
    total_water = tank1_water + tank2_water + tank3_water
    result = total_water
    return result

print(solution())