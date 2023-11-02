def solution():
    # Define the number of fleas after four treatments
    fleas_after = 14

    # Calculate the number of fleas before any treatments
    fleas_before = fleas_after * 2 ** 4

    # Calculate the difference between the number of fleas before and after treatments
    flea_difference = fleas_before - fleas_after
    result = flea_difference
    return result

print(solution())