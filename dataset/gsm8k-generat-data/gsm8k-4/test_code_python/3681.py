def solution():
    """The leak in Jerry's roof drips 3 drops a minute into the pot he put under it. Each drop is 20 ml, and the pot holds 3 liters. How long will it take the pot to be full?"""
    # Define the capacity of the pot in milliliters
    pot_capacity = 3000

    # Calculate the volume of water added per minute in milliliters
    water_per_min = 3 * 20

    # Calculate how long it will take to fill up the pot in minutes
    time_to_fill = pot_capacity / water_per_min

    result = time_to_fill
    return result

print(solution())