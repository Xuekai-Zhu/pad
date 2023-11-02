def solution():
    elvis_squares = 5
    ralph_squares = 3
    elvis_sticks = 4 * elvis_squares
    ralph_sticks = 8 * ralph_squares
    sticks_used = elvis_sticks + ralph_sticks
    sticks_left = 50 - sticks_used
    result = sticks_left
    return result

print(solution())