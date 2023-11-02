def solution():
    tank1_capacity = 7000  # Capacity of the first tank is 7000 gallons
    tank2_capacity = 5000  # Capacity of the second tank is 5000 gallons
    tank3_capacity = 3000  # Capacity of the third tank is 3000 gallons

    # Calculate the amount of water in each tank based on the given fill levels
    tank1_water = tank1_capacity * (3/4)
    tank2_water = tank2_capacity * (4/5)
    tank3_water = tank3_capacity * (1/2)

    # Calculate the total amount of water in all three tanks
    total_water = tank1_water + tank2_water + tank3_water
    result = total_water
    return result

print(solution())