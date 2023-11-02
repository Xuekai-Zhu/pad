def solution():
    # Define the number of eggplants and sunflowers in each packet
    eggplants_per_packet = 14
    sunflowers_per_packet = 10

    # Define the number of packets of each seed bought
    eggplant_packets = 4
    sunflower_packets = 6

    # Calculate the total number of eggplants and sunflowers
    total_eggplants = eggplants_per_packet * eggplant_packets
    total_sunflowers = sunflowers_per_packet * sunflower_packets

    # Calculate the total number of plants
    total_plants = total_eggplants + total_sunflowers
    result = total_plants
    return result

print(solution())