def solution():
    tank1_capacity = 7000
    tank2_capacity = 5000
    tank3_capacity = 3000

    # Calculate the amount of water in tank 1
    tank1_water = tank1_capacity * (3/4)
    
    # Calculate the amount of water in tank 2
    tank2_water = tank2_capacity * (4/5)

    # Calculate the amount of water in tank 3
    tank3_water = tank3_capacity * (1/2)

    # Calculate the total amount of water in all tanks
    total_water = tank1_water + tank2_water + tank3_water
    result = total_water
    return result

print(solution())