def solution():
    """Mr. Finnegan has 3 tanks with a capacity of 7000 gallons, 5000 gallons, and 3000 gallons, respectively. If he fills the first tank up to 3/4 full, the second tank with water up to 4/5 of its capacity, and the third tank up to half of its capacity, how many gallons in total are in the tanks?"""
    # Define the capacity of each tank
    capacity_1 = 7000
    capacity_2 = 5000
    capacity_3 = 3000

    # Calculate the amount of water in the first tank
    water_1 = capacity_1 * 3/4

    # Calculate the amount of water in the second tank
    water_2 = capacity_2 * 4/5

    # Calculate the amount of water in the third tank
    water_3 = capacity_3 * 1/2

    # Calculate the total amount of water in all tanks
    total_water = water_1 + water_2 + water_3

    # Display the total amount of water
    result = total_water
    return result

print(solution())