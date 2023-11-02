def solution():
    # Define the number of leis and flowers per lei
    num_leis = 4
    flowers_per_lei = 2.5 * 12  # convert 2.5 dozen to number of flowers

    # Calculate the total number of flowers needed
    total_flowers_needed = num_leis * flowers_per_lei
    result = total_flowers_needed
    return result

print(solution())