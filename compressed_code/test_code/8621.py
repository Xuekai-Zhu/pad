def solution():
    
    seed_to_fertilizer_ratio = 3
    total_gallons = 60
    total_parts = 1 + seed_to_fertilizer_ratio
    seed_parts = total_gallons / total_parts * seed_to_fertilizer_ratio
    result = seed_parts
    return result

print(solution())