def solution():
    """Carson is covering the high school football field with grass seed. Each square meter needs three times as much seed as fertilizer. If Carson uses 60 gallons of seed and fertilizer combined, how many gallons of seed does he use?"""
    total = 60
    seed_to_fertilizer_ratio = 3
    combined_ratio = seed_to_fertilizer_ratio + 1
    seed_gallons = (total / combined_ratio) * seed_to_fertilizer_ratio
    result = seed_gallons
    return result

print(solution())