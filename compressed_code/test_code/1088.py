def solution():
    
    first_group_snails = 3 * 5
    second_group_snails = 3 * 9
    total_first_two_groups_snails = first_group_snails + second_group_snails
    mother_duck_snails = 3 * total_first_two_groups_snails
    remaining_ducklings_snails = (8 - 6) * (0.5 * mother_duck_snails)
    total_snails = total_first_two_groups_snails + mother_duck_snails + remaining_ducklings_snails
    result = total_snails
    return result

print(solution())