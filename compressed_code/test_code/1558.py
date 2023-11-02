def solution():
    
    pearls_per_oyster = 0.25
    oysters_per_dive = 16
    pearls_needed = 56
    total_oysters_needed = pearls_needed / pearls_per_oyster
    total_dives_needed = total_oysters_needed / oysters_per_dive
    result = total_dives_needed
    return result

print(solution())