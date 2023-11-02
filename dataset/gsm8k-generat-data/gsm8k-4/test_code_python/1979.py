def solution():
    """Val cuts a single watermelon into 40 slices, and each slice has 20 black seeds and 20 white seeds. What is the total number of seeds in a watermelon?"""
    # Define the number of slices and seeds per slice
    slices = 40
    seeds_per_slice = 20 + 20

    # Calculate the total number of seeds
    total_seeds = slices * seeds_per_slice

    # return the result
    result = total_seeds
    return result

print(solution())