def solution():
    """Chris has twelve marbles, and Ryan has twenty-eight marbles. If they put marbles together in a pile and then each takes away 1/4 of marbles from the pile, calculate the number of marbles remaining in the pile."""
    # Define the number of marbles Chris and Ryan have
    CHRIS_MARBLES = 12
    RYAN_MARBLES = 28

    # Calculate the total number of marbles in the pile
    total_marbles = CHRIS_MARBLES + RYAN_MARBLES

    # Calculate the number of marbles each takes away
    marbles_taken = total_marbles / 4

    # Calculate the number of marbles remaining in the pile
    remaining_marbles = total_marbles - (2 * marbles_taken)

    # Display the number of marbles remaining
    result = remaining_marbles
    return result

print(solution())