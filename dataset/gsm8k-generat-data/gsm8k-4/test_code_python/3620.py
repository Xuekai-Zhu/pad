def solution():
    """The gauge on a water tank shows that the tank is 1/3 full of water. To fill the tank, 16 gallons of water are added. How many gallons of water does the tank hold when full?"""
    # Define the initial fraction of the tank that is full
    initial_fraction_full = 1/3

    # Define the amount of water added to fill the tank
    water_added = 16

    # Calculate the total amount of water in the tank when full
    total_water = water_added / (1 - initial_fraction_full)

    result = total_water
    return result

print(solution())