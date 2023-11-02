def solution():
    # Calculate the total number of pairs of shoes tried on by Helga
    total_pairs = 7  # Helga tried on 7 pairs of shoes at the first store
    total_pairs += 2 + 7  # Helga tried on 2 more pairs at the second store than at the first store
    total_pairs += 0  # Helga did not try on any shoes at the third store
    total_pairs += 2 * (7 + 2 + 0)  # Helga tried on twice as many pairs at the fourth store as at the other three stores combined
    total_pairs += 1  # Helga finally bought a pair of shoes

    result = total_pairs
    return result

print(solution())