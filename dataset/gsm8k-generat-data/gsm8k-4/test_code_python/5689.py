def solution():
    """If a bunny comes out of its burrow 3 times per minute, calculate the combined number of times 20 bunnies at the same pace will have come out of their burrows in 10 hours."""
    # Define the number of bunnies and the number of minutes in 10 hours
    NUM_BUNNIES = 20
    MINUTES_IN_10_HOURS = 10 * 60

    # Calculate the total number of times the bunnies come out of their burrows
    total_times = NUM_BUNNIES * 3 * MINUTES_IN_10_HOURS

    # Return the result
    result = total_times
    return result

print(solution())