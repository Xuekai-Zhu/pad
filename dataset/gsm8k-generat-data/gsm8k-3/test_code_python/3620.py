def solution():
    """The gauge on a water tank shows that the tank is 1/3 full of water. To fill the tank, 16 gallons of water are added. How many gallons of water does the tank hold when full?"""
    # Determine the fraction of the tank that has been filled
    filled_fraction = 1/3

    # Determine the amount of water needed to fill the tank
    # The tank must be filled with 1 - filled_fraction of its total capacity
    # 16 gallons of water have already been added to the tank
    # Therefore, the amount of water needed to fill the tank is
    # (1 - filled_fraction) * tank_capacity - 16
    # We can assume that the tank_capacity is a multiple of 3
    # and the total amount of water in the tank after it is filled is a whole number
    tank_capacity = 3 * 16 / (1 - filled_fraction)

    # Display the total capacity of the tank
    result = tank_capacity
    return result

print(solution())