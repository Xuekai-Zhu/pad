def solution():
    """There are 50 marbles in a box which has a mixture of white, red and blue marbles. There were originally 20 white marbles and an equal number of red and blue marbles. Jack removes a number of marbles equal to double the difference between the number of white marbles and the number of blue marbles. How many marbles are left in the box?"""
    # Define the number of white marbles, which is also equal to the number of red and blue marbles
    WHITE_MARBLES = 20

    # Calculate the number of red and blue marbles
    OTHER_MARBLES = (50 - WHITE_MARBLES) / 2

    # Calculate the difference between the number of white and blue marbles
    WHITE_BLUE_DIFF = abs(WHITE_MARBLES - OTHER_MARBLES)

    # Calculate the number of marbles Jack removes
    JACK_REMOVES = WHITE_BLUE_DIFF * 2

    # Calculate the number of marbles left in the box
    marbles_left = 50 - JACK_REMOVES

    # Display the number of marbles left in the box
    result = marbles_left
    return result

print(solution())