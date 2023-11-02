def solution():
    """Elvis and Ralph are to make square shapes with matchsticks from a box containing 50 matchsticks. Elvis makes 4-matchstick squares and Ralph makes 8-matchstick squares. If Elvis makes 5 squares and Ralph makes 3, how many matchsticks will be left in the box?"""
    # Define the number of matchsticks used for each square
    ELVIS_SQUARE = 4
    RALPH_SQUARE = 8

    # Define the number of squares made by Elvis and Ralph
    elvis_squares = 5
    ralph_squares = 3

    # Calculate the total number of matchsticks used
    total_matchsticks = (elvis_squares * ELVIS_SQUARE) + (ralph_squares * RALPH_SQUARE)

    # Calculate the number of matchsticks left in the box
    matchsticks_left = 50 - total_matchsticks

    # Display the number of matchsticks left in the box
    result = matchsticks_left
    return result

print(solution())