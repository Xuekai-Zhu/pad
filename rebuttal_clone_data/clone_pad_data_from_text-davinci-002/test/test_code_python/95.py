def solution():
    
    grams_per_packet = 100
    packets_sold = 20
    grams_per_kilogram = 1000
    total_grams = grams_per_packet * packets_sold
    total_kilograms = total_grams / grams_per_kilogram
    result = total_kilograms
    return result

print(solution())