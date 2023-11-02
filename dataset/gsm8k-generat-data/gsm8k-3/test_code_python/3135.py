def solution():
    """John is an eccentric millionaire.  He decides to fill his swimming pool with bottled water.  A cubic foot of water is 25 liters.  His pool is 10 feet deep and 6 feet by 20 feet. A liter of water costs $3. How much does it cost to fill the pool?"""
    # Calculate the volume of the pool
    pool_volume = 10 * 6 * 20  # height x width x length in feet
    pool_volume_liters = pool_volume * 25  # volume in liters

    # Calculate the cost of filling the pool with bottled water
    water_cost = pool_volume_liters * 3

    # Display the cost of filling the pool with bottled water
    result = water_cost
    return result

print(solution())