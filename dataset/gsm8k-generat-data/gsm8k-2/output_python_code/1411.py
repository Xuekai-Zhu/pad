def solution():
    """A mother duck as 8 ducklings. The first 3 ducklings find 5 snails each. Another 3 ducklings find 9 snails each, and the remaining ducklings each find half the number of snails that mother duck finds. If mother duck finds tree times the total number of snails as the first 2 groups of ducklings, how many snails does the family of ducks have collectively?"""
    first_group_snails = 3 * 5
    second_group_snails = 3 * 9
    total_first_two_groups_snails = first_group_snails + second_group_snails
    mother_duck_snails = 3 * total_first_two_groups_snails
    remaining_ducklings_snails = (8 - 6) * (0.5 * mother_duck_snails)
    total_snails = total_first_two_groups_snails + mother_duck_snails + remaining_ducklings_snails
    result = total_snails
    return result

print(solution())