def solution():
    # Let x be the first number
    # Let y be the second number
    # We know that x + y = 33 and y = 2x
    x = (1/3) * 33  # solve for x: (33 - y) / 2 = x and substitute y = 2x
    y = 2 * x  # solve for y
    result = y
    return result

print(solution())