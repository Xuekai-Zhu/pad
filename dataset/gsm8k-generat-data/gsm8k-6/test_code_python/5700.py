def solution():
    # Calculate the number of snack eaters after each step
    initial_snack_eaters = 100
    after_new_outsiders = initial_snack_eaters + 20
    after_half_full_left = (after_new_outsiders // 2) + 10
    after_30_more_full_left = after_half_full_left - 30
    remaining_snack_eaters = after_30_more_full_left // 2

    result = remaining_snack_eaters
    return result

print(solution())