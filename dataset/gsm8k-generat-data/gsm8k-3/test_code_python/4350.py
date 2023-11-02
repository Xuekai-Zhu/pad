def solution():
    """Out of the 500 marbles that Cindy had, she gave her four friends 80 marbles each. What's four times the number of marbles she has remaining?"""
    # Define the total number of marbles that Cindy had
    total_marbles = 500

    # Subtract the marbles given to her friends
    remaining_marbles = total_marbles - (80 * 4)

    # Calculate four times the remaining marbles
    result = 4 * remaining_marbles
    return result

print(solution())