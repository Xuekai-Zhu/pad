def solution():
    """Val cuts a single watermelon into 40 slices, and each slice has 20 black seeds and 20 white seeds. What is the total number of seeds in a watermelon?"""
    # Define the number of slices in a watermelon
    slices = 40

    # Define the number of seeds in a single slice
    black_seeds = 20
    white_seeds = 20

    # Calculate the total number of seeds in a watermelon
    total_seeds = slices * (black_seeds + white_seeds)

    # Display the total number of seeds
    result = total_seeds
    return result

print(solution())