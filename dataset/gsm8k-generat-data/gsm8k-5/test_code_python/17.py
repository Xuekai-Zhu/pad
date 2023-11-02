def solution():
    # Total number of hard hats in the truck
    total_hard_hats = 26 + 15 + 24

    # Number of pink hard hats taken away
    pink_taken = 4 + 6

    # Number of green hard hats taken away
    green_taken = 2 * 6  # Twice the number of pink hard hats taken away

    # Calculate the number of hard hats remaining in the truck
    remaining_hard_hats = total_hard_hats - pink_taken - green_taken

    result = remaining_hard_hats
    return result

print(solution())