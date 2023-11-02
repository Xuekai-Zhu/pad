def solution():
    """Carter grew 9 plants with 3 seed packets. How many more seed packets does Carter need to have a total of 12 plants in his backyard?"""
    current_plants = 9
    desired_plants = 12
    plants_per_packet = current_plants / 3
    needed_packets = (desired_plants - current_plants) / plants_per_packet
    result = needed_packets
    return result

print(solution())