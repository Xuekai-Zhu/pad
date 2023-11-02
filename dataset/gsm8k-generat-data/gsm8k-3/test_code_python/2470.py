def solution():
    """David and Brenda are playing Scrabble. Brenda is ahead by 22 points when she makes a 15-point play. David responds with a 32-point play. By how many points is Brenda now ahead?"""
    # Define the initial point difference
    INITIAL_DIFFERENCE = 22

    # Define the points earned by each player in their plays
    BRENDA_PLAY = 15
    DAVID_PLAY = 32

    # Calculate the new point difference after the plays
    new_difference = INITIAL_DIFFERENCE + BRENDA_PLAY - DAVID_PLAY

    # Display the new point difference
    result = new_difference
    return result

print(solution())