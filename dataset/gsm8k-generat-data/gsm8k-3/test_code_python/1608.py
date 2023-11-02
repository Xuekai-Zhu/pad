def solution():
    """Carter grew 9 plants with 3 seed packets. How many more seed packets does Carter need to have a total of 12 plants in his backyard?"""
    # Define the number of plants per seed packet
    PLANTS_PER_PACKET = 3

    # Calculate the number of seed packets needed for 12 plants
    packets_needed = (12 - 9) / PLANTS_PER_PACKET

    # Round up to the nearest whole number of seed packets
    packets_needed = math.ceil(packets_needed)

    # Display the number of additional seed packets needed
    result = packets_needed
    return result

print(solution())