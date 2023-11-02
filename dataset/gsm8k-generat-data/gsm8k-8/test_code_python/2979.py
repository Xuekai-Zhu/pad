def solution():
    # Set up the equations
    b = 2 * s
    d = 3 * b
    total_guitars = s + b + d

    # Solve for s
    s = total_guitars / 8

    # Use s to solve for d
    d = 3 * 2 * s

    result = d
    return result

print(solution())