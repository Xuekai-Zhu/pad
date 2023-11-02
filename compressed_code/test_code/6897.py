def solution():
    
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