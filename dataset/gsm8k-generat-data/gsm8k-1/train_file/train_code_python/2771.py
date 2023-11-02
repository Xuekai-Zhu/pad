def solution():
    """Shyne can grow 14 eggplants in every seed packet and 10 sunflowers in every seed packet. She bought 4 seed packets of eggplants and 6 seed packets of sunflower, how many plants can Shyne grow in her backyard?"""
    eggplants_per_packet = 14
    sunflowers_per_packet = 10
    eggplant_packets = 4
    sunflower_packets = 6
    total_eggplants = eggplants_per_packet * eggplant_packets
    total_sunflowers = sunflowers_per_packet * sunflower_packets
    total_plants = total_eggplants + total_sunflowers
    result = total_plants
    return result

print(solution())