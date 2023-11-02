def solution():
    """
    Elvis and Ralph are to make square shapes with matchsticks from a box containing 50 matchsticks. 
    Elvis makes 4-matchstick squares and Ralph makes 8-matchstick squares. 
    If Elvis makes 5 squares and Ralph makes 3, how many matchsticks will be left in the box?
    """
    total_matchsticks = 50
    elvis_squares = 5
    ralph_squares = 3
    elvis_matchsticks = elvis_squares * 4
    ralph_matchsticks = ralph_squares * 8
    used_matchsticks = elvis_matchsticks + ralph_matchsticks
    remaining_matchsticks = total_matchsticks - used_matchsticks
    result = remaining_matchsticks
    return result

print(solution())