def solution():
    """25% of oysters have pearls in them. Jamie can collect 16 oysters during each dive. How many dives does he have to make to collect 56 pearls?"""
    pearls_per_oyster = 0.25
    oysters_per_dive = 16
    pearls_needed = 56
    total_oysters_needed = pearls_needed / pearls_per_oyster
    total_dives_needed = total_oysters_needed / oysters_per_dive
    result = total_dives_needed
    return result

print(solution())