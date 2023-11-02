def solution():
    # Calculate the total number of snails found by the first 2 groups of ducks
    snails_first_group = 3 * 5  # first 3 ducklings find 5 snails each
    snails_second_group = 3 * 9  # another 3 ducklings find 9 snails each
    total_first_two_groups = snails_first_group + snails_second_group

    # Calculate the total number of snails found by mother duck and the remaining ducklings
    snails_mother_duck = total_first_two_groups * 3  # mother duck finds three times the total number of snails as the first 2 groups
    snails_remaining_ducklings = 8 - 3 - 3  # remaining ducklings are 8 - 3 - 3
    snails_remaining_ducklings_each = snails_mother_duck / 2  # each remaining duckling finds half the snails that mother duck finds
    total_remaining_ducklings = snails_remaining_ducklings * snails_remaining_ducklings_each

    # Calculate the total number of snails found by the family of ducks
    total_snails = total_first_two_groups + snails_mother_duck + total_remaining_ducklings
    result = total_snails
    return result

print(solution())