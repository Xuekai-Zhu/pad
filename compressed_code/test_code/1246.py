def solution():
    
    plants_per_packet = 3
    total_plants = 12
    current_plants = 9
    plants_needed = total_plants - current_plants
    seed_packets_needed = (plants_needed + (plants_per_packet - 1)) // plants_per_packet
    result = seed_packets_needed
    return result

print(solution())