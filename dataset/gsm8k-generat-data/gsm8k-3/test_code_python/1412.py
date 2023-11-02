def solution():
    """A mother duck as 8 ducklings. The first 3 ducklings find 5 snails each. Another 3 ducklings find 9 snails each, and the remaining ducklings each find half the number of snails that mother duck finds. If mother duck finds tree times the total number of snails as the first 2 groups of ducklings, how many snails does the family of ducks have collectively?"""
    # Define the number of ducklings and the number of snails found by each group
    NUM_DUCKLINGS = 8
    GROUP1_SNAILS = 3 * 5
    GROUP2_SNAILS = 3 * 9

    # Calculate the number of snails found by the remaining ducklings
    remaining_ducklings = NUM_DUCKLINGS - 6
    remaining_snailes = 0.5 * GROUP2_SNAILS

    # Calculate the number of snails found by mother duck
    mother_snailes = 3 * (GROUP1_SNAILES + GROUP2_SNAILES)

    # Calculate the total number of snails found by the family
    total_snailes = GROUP1_SNAILES + GROUP2_SNAILES + remaining_snailes + mother_snailes

    # Display the total number of snails found by the family
    result = total_snailes
    return result

print(solution())