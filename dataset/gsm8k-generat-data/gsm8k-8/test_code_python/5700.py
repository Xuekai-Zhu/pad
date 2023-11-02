def solution():
    # Calculate the number of people who had snacks
    snack_eaters = 100 + 20
    half_snack_eaters_leave = snack_eaters // 2
    remaining_snack_eaters = snack_eaters - half_snack_eaters_leave

    # Calculate the number of people who joined for snacks later
    new_snack_eaters = 10

    # Calculate the number of people who left after getting full
    full_snack_eaters = 30
    remaining_snack_eaters -= full_snack_eaters

    # Calculate the number of people who left after half of remaining snack eaters left
    remaining_snack_eaters //= 2

    result = remaining_snack_eaters
    return result

print(solution())