def solution():
    """A mother duck as 8 ducklings. The first 3 ducklings find 5 snails each. Another 3 ducklings find 9 snails each,
    and the remaining ducklings each find half the number of snails that mother duck finds.
    If mother duck finds tree times the total number of snails as the first 2 groups of ducklings,
    how many snails does the family of ducks have collectively?"""
    first_group_snails = 5 * 3
    second_group_snails = 9 * 3
    total_first_two_groups_snails = first_group_snails + second_group_snails
    mother_duck_snails = total_first_two_groups_snails * 3
    remaining_ducklings = 8 - 3 - 3
    each_remaining_snails = mother_duck_snails / 2
    total_remaining_snails = each_remaining_snails * remaining_ducklings
    total_snails = total_first_two_groups_snails + mother_duck_snails + total_remaining_snails
    result = total_snails
    return result

print(solution())