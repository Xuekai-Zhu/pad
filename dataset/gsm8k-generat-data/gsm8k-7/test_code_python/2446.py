def solution():
    bob_skips = 12
    jim_skips = 15
    num_rocks = 10

    # Calculate Bob's total skips
    bob_total_skips = bob_skips * num_rocks

    # Calculate Jim's total skips
    jim_total_skips = jim_skips * num_rocks

    # Calculate the total skips
    total_skips = bob_total_skips + jim_total_skips
    result = total_skips
    return result

print(solution())