def solution():
    # Let f, s, and t be the distances (in meters) of his first, second, and third throws respectively.
    # We know that f = 2s and f/2 = t, and that f + s + t = 1050
    # Substitute for t and simplify the equation to get:
    f + f/4 = 1050
    # Solve for f to get:
    f = 840

    result = f
    return result

print(solution())