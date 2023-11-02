def solution():
    """If a bunny comes out of its burrow 3 times per minute, calculate the combined number of times 20 bunnies at the same pace will have come out of their burrows in 10 hours."""
    # Define the number of bunnies and their burrow rate
    bunnies = 20
    burrow_rate = 3 # times per minute

    # Calculate the total number of times the bunnies come out of their burrows in 10 hours
    minutes = 10 * 60 # 10 hours in minutes
    total_burrows = bunnies * burrow_rate * minutes

    # Display the total number of burrows
    result = total_burrows
    return result

print(solution())