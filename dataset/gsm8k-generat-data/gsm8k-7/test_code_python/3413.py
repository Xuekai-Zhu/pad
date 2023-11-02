def solution():
    # Initialize variables
    left_birds_seeds = 20
    right_birds_seeds = 0
    extra_birds_seeds = 30
    leftover_seeds = 30
    total_seeds = 0

    # Calculate the number of seeds thrown to the bigger group of birds on the right
    right_birds_seeds = left_birds_seeds * 2

    # Calculate the total number of seeds before extra birds join
    total_seeds = left_birds_seeds + right_birds_seeds

    # Add the seeds for the extra birds
    total_seeds += extra_birds_seeds

    # Subtract the leftover seeds
    total_seeds += leftover_seeds

    result = total_seeds
    return result

print(solution())