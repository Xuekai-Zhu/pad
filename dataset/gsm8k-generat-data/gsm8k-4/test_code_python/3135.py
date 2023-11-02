def solution():
    """John is an eccentric millionaire. He decides to fill his swimming pool with bottled water. A cubic foot of water is 25 liters. His pool is 10 feet deep and 6 feet by 20 feet. A liter of water costs $3. How much does it cost to fill the pool?"""
    # Define the dimensions of the pool
    depth = 10  # feet
    length = 6  # feet
    width = 20  # feet

    # Calculate the volume of the pool in cubic feet
    volume = depth * length * width

    # Convert the volume to liters
    volume_liters = volume * 25

    # Calculate the cost of filling the pool
    cost = volume_liters * 3

    # Return the result
    result = cost
    return result

print(solution())