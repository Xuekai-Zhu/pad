def solution():
    """Shyne can grow 14 eggplants in every seed packet and 10 sunflowers in every seed packet. She bought 4 seed packets of eggplants and 6 seed packets of sunflower, how many plants can Shyne grow in her backyard? """
    # Define the number of plants in each seed packet
    EGGPLANT_PER_PACKET = 14
    SUNFLOWER_PER_PACKET = 10

    # Define the number of seed packets purchased
    eggplant_packets = 4
    sunflower_packets = 6

    # Calculate the total number of eggplants and sunflowers
    total_eggplants = eggplant_packets * EGGPLANT_PER_PACKET
    total_sunflowers = sunflower_packets * SUNFLOWER_PER_PACKET

    # Calculate the total number of plants
    total_plants = total_eggplants + total_sunflowers

    # return the result
    result = total_plants
    return result

print(solution())