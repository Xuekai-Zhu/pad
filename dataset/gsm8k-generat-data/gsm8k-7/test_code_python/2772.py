def solution():
    eggplant_per_packet = 14
    sunflower_per_packet = 10

    num_eggplant_packets = 4
    num_sunflower_packets = 6

    # Calculate the total number of eggplants that can be grown
    total_eggplants = eggplant_per_packet * num_eggplant_packets

    # Calculate the total number of sunflowers that can be grown
    total_sunflowers = sunflower_per_packet * num_sunflower_packets

    # Calculate the total number of plants that can be grown
    total_plants = total_eggplants + total_sunflowers
    result = total_plants
    return result

print(solution())