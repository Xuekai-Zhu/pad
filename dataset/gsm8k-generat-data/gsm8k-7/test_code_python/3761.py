def solution():
    num_treatments = 4
    final_flea_count = 14

    # Calculate the total number of fleas before any treatments
    starting_flea_count = final_flea_count * 2 ** num_treatments

    # Calculate the difference between the starting and final flea counts
    flea_difference = starting_flea_count - final_flea_count
    result = flea_difference
    return result

print(solution())