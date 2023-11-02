def solution():
    total_matchsticks = 50  # The box contains 50 matchsticks
    elvis_squares = 5  # Elvis makes 5 squares with 4 matchsticks each
    ralph_squares = 3  # Ralph makes 3 squares with 8 matchsticks each

    # Calculate the total number of matchsticks used by Elvis and Ralph
    elvis_matchsticks = elvis_squares * 4
    ralph_matchsticks = ralph_squares * 8
    total_used = elvis_matchsticks + ralph_matchsticks

    # Calculate the number of matchsticks left in the box
    matchsticks_left = total_matchsticks - total_used
    result = matchsticks_left
    return result

print(solution())