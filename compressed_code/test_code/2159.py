def solution():
    
    
    eggplant_per_packet = 14
    sunflower_per_packet = 10
    eggplant_packets = 4
    sunflower_packets = 6
    
    total_eggplants = eggplant_per_packet * eggplant_packets
    total_sunflowers = sunflower_per_packet * sunflower_packets
    
    plants_in_backyard = total_eggplants + total_sunflowers
    
    result = plants_in_backyard
    return result

print(solution())