def solution():
    # Calculate the snails found by the first group of ducklings
    group1_snails = 3 * 5

    # Calculate the snails found by the second group of ducklings
    group2_snails = 3 * 9

    # Calculate the snails found by the remaining ducklings
    group3_snails = 0.5 * (tree_ducks - 3 * 5 - 3 * 9)

    # Calculate the total number of snails found
    total_snails = group1_snails + group2_snails + group3_snails + 3 * group1_snails

    result = total_snails
    return result

print(solution())