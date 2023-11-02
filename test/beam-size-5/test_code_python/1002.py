def solution():
    
    # Define the dimensions of the pool
    width = 14
    length = 25
    depth = 4

    # Calculate the volume of the pool
    volume = width * length * depth

    # Calculate the amount of water needed to fill the pool
    water_needed = volume / 5.9

    # Calculate the cost to fill the pool
    cost = water_needed * 0.10

    # Display the cost to fill the pool
    result = cost
    return result

print(solution())