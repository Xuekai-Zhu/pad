def solution():
    # Codger needs 3 shoes to make a complete set
    shoes_per_set = 3

    # Codger already has 1 complete set, so he needs to buy 4 more sets
    sets_needed = 4

    # Each set requires 2 pairs of shoes, so Codger needs to buy 2 * sets_needed pairs of shoes
    pairs_needed = 2 * sets_needed

    # However, Codger already has 1 pair of shoes (2 shoes), so he only needs to buy pairs_needed - 1 pairs of shoes
    total_pairs_needed = pairs_needed - 1
    result = total_pairs_needed
    return result

print(solution())