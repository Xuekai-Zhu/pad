def solution():
    mother_ducklings = 8  # There are 8 ducklings in total
    first_group = 3  # The first 3 ducklings find 5 snails each
    second_group = 3  # Another 3 ducklings find 9 snails each
    third_group = 2  # The remaining 2 ducklings each find half the number of snails that mother duck finds

    # Calculate the total number of snails found by the first group of ducklings
    snails_first_group = 5 * first_group

    # Calculate the total number of snails found by the second group of ducklings
    snails_second_group = 9 * second_group

    # Calculate the total number of snails found by the third group of ducklings
    snails_third_group = 0.5 * (snails_first_group + snails_second_group)

    # Calculate the total number of snails found by mother duck
    snails_mother = 3 * (snails_first_group + snails_second_group)

    # Calculate the total number of snails found by the family of ducks
    total_snails = snails_first_group + snails_second_group + snails_third_group + snails_mother
    result = total_snails
    return result

print(solution())