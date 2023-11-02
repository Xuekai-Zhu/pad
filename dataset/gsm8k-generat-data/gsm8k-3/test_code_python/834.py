def solution():
    """Eric has 20 marbles. He has 12 white marbles, 6 blue marbles, and the rest are green marbles. How many green marbles does Eric have?"""
    # Define the number of white and blue marbles
    white_marbles = 12
    blue_marbles = 6

    # Calculate the number of green marbles
    green_marbles = 20 - white_marbles - blue_marbles

    # Display the number of green marbles
    result = green_marbles
    return result

print(solution())