def solution():
    num_shoes_owned = 3
    shoes_per_set = 3
    num_sets_needed = 5

    # Calculate the total number of shoes needed to have 5 complete sets
    total_shoes_needed = num_sets_needed * shoes_per_set

    # Calculate the number of pairs of shoes needed (assuming 2 shoes per pair)
    num_pairs_needed = (total_shoes_needed - num_shoes_owned) // 2

    result = num_pairs_needed
    return result

print(solution())