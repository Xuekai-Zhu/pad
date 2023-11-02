def solution():
    """Elvis and Ralph are to make square shapes with matchsticks from a box containing 50 matchsticks. Elvis makes 4-matchstick squares and Ralph makes 8-matchstick squares. If Elvis makes 5 squares and Ralph makes 3, how many matchsticks will be left in the box?"""
    # Define the number of matchsticks needed for each square
    elvis_matchsticks = 4
    ralph_matchsticks = 8

    # Define the number of squares each person makes
    elvis_squares = 5
    ralph_squares = 3

    # Calculate the total number of matchsticks used by each person
    elvis_total_matchsticks = elvis_matchsticks * elvis_squares
    ralph_total_matchsticks = ralph_matchsticks * ralph_squares

    # Calculate the total number of matchsticks used
    total_matchsticks_used = elvis_total_matchsticks + ralph_total_matchsticks

    # Calculate the number of matchsticks left in the box
    matchsticks_left = 50 - total_matchsticks_used

    # Return the result
    result = matchsticks_left
    return result

print(solution())