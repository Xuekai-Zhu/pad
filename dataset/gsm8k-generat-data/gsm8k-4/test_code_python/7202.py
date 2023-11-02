def solution():
    """Chris has twelve marbles, and Ryan has twenty-eight marbles. If they put marbles together in a pile and then each takes away 1/4 of marbles from the pile, calculate the number of marbles remaining in the pile."""
    # Define the initial number of marbles
    initial_marbles = 12 + 28

    # Calculate the number of marbles taken away by each person
    marbles_taken = initial_marbles * (1/4)

    # Calculate the number of marbles remaining in the pile
    marbles_remaining = initial_marbles - (2 * marbles_taken)

    # return the result
    result = marbles_remaining
    return result

print(solution())