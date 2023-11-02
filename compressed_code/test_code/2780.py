def solution():
    
    total = 60
    seed_to_fertilizer_ratio = 3
    combined_ratio = seed_to_fertilizer_ratio + 1
    seed_gallons = (total / combined_ratio) * seed_to_fertilizer_ratio
    result = seed_gallons
    return result

print(solution())