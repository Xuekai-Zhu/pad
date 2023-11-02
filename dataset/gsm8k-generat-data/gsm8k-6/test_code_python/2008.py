def solution():
    # Calculate the number of oysters Jamie needs to collect to get 56 pearls
    total_oysters_needed = 56 / 0.25  # 25% of oysters have pearls, so Jamie needs 4 oysters to get 1 pearl
    # Calculate the number of dives needed to collect the required number of oysters
    dives_needed = total_oysters_needed / 16  # Jamie can collect 16 oysters during each dive
    result = dives_needed
    return result

print(solution())