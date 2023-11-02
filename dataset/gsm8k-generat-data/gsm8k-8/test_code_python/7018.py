def solution():
    # Calculate the total matchsticks used by Elvis and Ralph
    elvis_matchsticks = 4 * 5
    ralph_matchsticks = 8 * 3
    total_matchsticks = elvis_matchsticks + ralph_matchsticks

    # Calculate the matchsticks left in the box
    matchsticks_left = 50 - total_matchsticks
    result = matchsticks_left
    return result

print(solution())