def solution():
    num_ducklings = 8
    first_group_snails = 5
    second_group_snails = 9
    mother_duck_multiple = 3

    # Calculate the total number of snails found by the first group of ducklings
    first_group_total_snails = 3 * first_group_snails

    # Calculate the total number of snails found by the second group of ducklings
    second_group_total_snails = 3 * second_group_snails

    # Calculate the number of snails found by each of the remaining ducklings
    remaining_ducklings_snails = (1/2) * mother_duck_multiple * (first_group_total_snails + second_group_total_snails)

    # Calculate the total number of snails found by all the ducklings
    total_snails = first_group_total_snails + second_group_total_snails + remaining_ducklings_snails

    # Calculate the total number of snails found by the mother duck
    mother_duck_snails = mother_duck_multiple * (first_group_total_snails + second_group_total_snails)

    # Calculate the grand total number of snails found by the family of ducks
    grand_total_snails = total_snails + mother_duck_snails
    result = grand_total_snails
    return result

print(solution())