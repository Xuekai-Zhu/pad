def solution():
    """25% of oysters have pearls in them. Jamie can collect 16 oysters during each dive.
    How many dives does he have to make to collect 56 pearls?"""
    # Calculate the number of pearls per dive
    pearls_per_dive = 16 * 0.25

    # Calculate the number of dives needed to collect 56 pearls
    dives_needed = 56 / pearls_per_dive

    # Round up to the nearest integer
    dives_needed = int(round(dives_needed, 0))

    # Display the number of dives needed
    result = dives_needed
    return result

print(solution())