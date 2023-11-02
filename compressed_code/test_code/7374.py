def solution():
    
    p_oysters = 0.25
    oysters_per_dive = 16
    pearls_needed = 56
    oysters_needed = pearls_needed / p_oysters
    dives_needed = oysters_needed / oysters_per_dive
    result = dives_needed
    return result

print(solution())