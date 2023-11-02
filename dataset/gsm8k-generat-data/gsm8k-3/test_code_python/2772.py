def solution():
    """Shyne can grow 14 eggplants in every seed packet and 10 sunflowers in every seed packet. She bought 4 seed packets of eggplants and 6 seed packets of sunflowers, how many plants can Shyne grow in her backyard?"""
    # Define the number of plants per seed packet
    EGGPLANT_PER_PACKET = 14
    SUNFLOWER_PER_PACKET = 10

    # Define the number of seed packets purchased
    eggplant_packets = 4
    sunflower_packets = 6

    # Calculate the total number of plants grown
    total_plants = (eggplant_packets * EGGPLANT_PER_PACKET) + (sunflower_packets * SUNFLOWER_PER_PACKET)

    # Display the total number of plants grown
    result = total_plants
    return result

print(solution())