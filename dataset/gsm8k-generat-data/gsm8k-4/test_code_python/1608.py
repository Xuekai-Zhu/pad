def solution():
    """Carter grew 9 plants with 3 seed packets. How many more seed packets does Carter need to have a total of 12 plants in his backyard?"""
    # Define the initial number of plants and seed packets
    initial_plants = 9
    initial_seed_packets = 3

    # Define the target number of plants
    target_plants = 12

    # Calculate the number of additional plants needed
    additional_plants = target_plants - initial_plants

    # Calculate the number of additional seed packets needed
    additional_seed_packets = additional_plants / 3

    # Round up the additional seed packets to the nearest integer
    additional_seed_packets = math.ceil(additional_seed_packets)

    # return the result
    result = additional_seed_packets
    return result

print(solution())