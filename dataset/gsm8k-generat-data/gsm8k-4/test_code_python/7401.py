def solution():
    """Mr. Finnegan has 3 tanks with a capacity of 7000 gallons, 5000 gallons, and 3000 gallons, respectively. If he fills the first tank up to 3/4 full, the second tank with water up to 4/5 of its capacity, and the third tank up to half of its capacity, how many gallons in total are in the tanks?"""
    # Define the capacities of the tanks
    tank1_capacity = 7000
    tank2_capacity = 5000
    tank3_capacity = 3000

    # Calculate the amount of water in each tank
    tank1_water = tank1_capacity * (3/4)
    tank2_water = tank2_capacity * (4/5)
    tank3_water = tank3_capacity * (1/2)

    # Calculate the total amount of water
    total_water = tank1_water + tank2_water + tank3_water

    # return the result
    result = total_water
    return result

print(solution())