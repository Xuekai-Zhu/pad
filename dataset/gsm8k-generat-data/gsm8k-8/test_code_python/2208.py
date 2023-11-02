def solution():
    # Define the length of each type of wood
    tall_wood_length = 4
    short_wood_length = 2

    # Define the number of each type of wood needed
    tall_wood_needed = 6
    short_wood_needed = 2

    # Calculate the total length of all the wood needed
    total_wood_length = (tall_wood_length * tall_wood_needed) + (short_wood_length * short_wood_needed)

    result = total_wood_length
    return result

print(solution())