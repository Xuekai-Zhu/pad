def solution():
    # Define the initial number of daisies Kylie has
    num_daisies = 5

    # Add the 9 daisies her sister gave her
    num_daisies += 9

    # Calculate half of her total daisies
    half_daisies = num_daisies / 2

    # Subtract the half daisies from the total
    num_daisies_left = num_daisies - half_daisies

    result = num_daisies_left
    return result

print(solution())