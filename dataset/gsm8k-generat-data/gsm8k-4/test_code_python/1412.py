def solution():
    """A mother duck as 8 ducklings. The first 3 ducklings find 5 snails each. Another 3 ducklings find 9 snails each, and the remaining ducklings each find half the number of snails that mother duck finds. If mother duck finds tree times the total number of snails as the first 2 groups of ducklings, how many snails does the family of ducks have collectively?"""
    # Define the number of ducklings and the snail count for each group of ducklings
    num_ducklings = 8
    snails_1 = 3 * 5
    snails_2 = 3 * 9
    snails_3 = 0.5 * snails_2
    
    # Calculate the snail count for mother duck
    snails_mother = 3 * (snails_1 + snails_2)

    # Calculate the total snail count for the family of ducks
    total_snails = snails_1 + snails_2 + snails_3 + snails_mother + num_ducklings

    result = total_snails
    return result

print(solution())