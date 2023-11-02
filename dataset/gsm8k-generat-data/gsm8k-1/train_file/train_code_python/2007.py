def solution():
    """25% of oysters have pearls in them. Jamie can collect 16 oysters during each dive. How many dives does he have to make to collect 56 pearls?"""
    p_oysters = 0.25
    oysters_per_dive = 16
    pearls_needed = 56
    oysters_needed = pearls_needed / p_oysters
    dives_needed = oysters_needed / oysters_per_dive
    result = dives_needed
    return result

print(solution())