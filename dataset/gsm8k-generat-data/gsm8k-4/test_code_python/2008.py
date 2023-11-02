def solution():
    """25% of oysters have pearls in them. Jamie can collect 16 oysters during each dive. How many dives does he have to make to collect 56 pearls?"""
    # Calculate the number of oysters needed to collect 56 pearls
    oysters_needed = 56 / 0.25

    # Calculate the number of dives needed to collect the required number of oysters
    dives_needed = oysters_needed / 16

    # Round up to get the minimum number of dives needed
    result = math.ceil(dives_needed)
    return result

print(solution())