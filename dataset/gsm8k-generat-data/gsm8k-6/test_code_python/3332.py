def solution():
    # Let x be the number of times Jason steps on his partner's feet
    # Then Nancy steps on her partner's feet 3x times
    # Total number of times they step on each other's feet is x + 3x + 32 = 4x + 32
    # Therefore, x = (32 - 3x)/4
    # Simplifying the equation, we get:
    x = 8 - (3/4)*x

    # Solving for x:
    x = 8
    result = x
    return result

print(solution())