def solution():
    
    packets_per_week = 20
    grams_per_packet = 100
    total_grams = packets_per_week * grams_per_packet
    total_kilos = total_grams / 1000
    result = total_kilos
    return result

print(solution())