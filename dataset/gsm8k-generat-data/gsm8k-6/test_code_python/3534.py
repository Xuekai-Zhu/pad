def solution():
    # Set up the equations based on the given information
    # Let q = number of quarters, d = number of dimes, n = number of nickels
    # We have 3 equations:
    # d = q + 3
    # n = q - 6
    # q + d + n = 63
    # Substituting the first two equations into the third equation, we get:
    # q + (q + 3) + (q - 6) = 63
    # Solving for q, we get:
    # 3q - 3 = 63
    # 3q = 66
    # q = 22

    # Therefore, John has 22 quarters
    result = 22
    return result

print(solution())