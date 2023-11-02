def solution():
    # Calculate the total number of matchsticks used by Elvis and Ralph
    elvis_matchsticks = 4 * 5  # Elvis makes 5 4-matchstick squares
    ralph_matchsticks = 8 * 3  # Ralph makes 3 8-matchstick squares
    total_matchsticks = elvis_matchsticks + ralph_matchsticks  # total matchsticks used

    # Calculate the number of matchsticks remaining in the box
    remaining_matchsticks = 50 - total_matchsticks
    result = remaining_matchsticks
    return result

print(solution())