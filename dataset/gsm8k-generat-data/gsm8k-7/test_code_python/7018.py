def solution():
    total_matchsticks = 50
    elvis_squares = 5
    ralph_squares = 3
    elvis_square_matchsticks = 4
    ralph_square_matchsticks = 8

    # Calculate the total number of matchsticks used by Elvis
    elvis_matchsticks = elvis_squares * elvis_square_matchsticks

    # Calculate the total number of matchsticks used by Ralph
    ralph_matchsticks = ralph_squares * ralph_square_matchsticks

    # Calculate the total number of matchsticks used
    total_used_matchsticks = elvis_matchsticks + ralph_matchsticks

    # Calculate the number of matchsticks left in the box
    matchsticks_left = total_matchsticks - total_used_matchsticks
    result = matchsticks_left
    return result

print(solution())