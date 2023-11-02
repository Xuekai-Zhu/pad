def solution():
    pearl_percentage = 0.25  # 25% of oysters have pearls
    oysters_per_dive = 16  # Jamie collects 16 oysters per dive
    pearls_per_dive = pearl_percentage * oysters_per_dive  # On average, Jamie collects 4 pearls per dive
    desired_pearls = 56  # Jamie wants to collect 56 pearls

    # Calculate the number of dives Jamie needs to make to collect 56 pearls
    dives_needed = desired_pearls / pearls_per_dive
    result = dives_needed
    return result

print(solution())