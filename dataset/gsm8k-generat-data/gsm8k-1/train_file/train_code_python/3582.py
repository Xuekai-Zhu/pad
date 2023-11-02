def solution():
    """Carson is covering the high school football field with grass seed. Each square meter needs three times as much seed as fertilizer. If Carson uses 60 gallons of seed and fertilizer combined, how many gallons of seed does he use?"""
    seed_to_fertilizer_ratio = 3
    total_gallons = 60
    total_parts = 1 + seed_to_fertilizer_ratio
    seed_parts = total_gallons / total_parts * seed_to_fertilizer_ratio
    result = seed_parts
    return result

print(solution())