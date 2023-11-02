def solution():
    """Chris has twelve marbles, and Ryan has twenty-eight marbles. If they put marbles together in a pile and then each takes away 1/4 of marbles from the pile, calculate the number of marbles remaining in the pile."""
    total_marbles = 12 + 28
    marbles_taken = (1/4) * total_marbles * 2
    marbles_remaining = total_marbles - marbles_taken
    result = marbles_remaining
    return result

print(solution())