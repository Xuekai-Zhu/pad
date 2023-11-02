def solution():
    """Jake sold 10 more stuffed animals than Thor. Quincy sold ten times as many stuffed animals as Thor. If Quincy sold 200 stuffed animals, how many more stuffed animals did Quincy sell than Jake?"""
    # Let's assume that Thor sold x stuffed animals
    thor = x

    # Jake sold 10 more than Thor
    jake = thor + 10

    # Quincy sold ten times as many as Thor
    quincy = 200

    # Calculate how many stuffed animals Thor sold
    x = quincy / 10
    
    # Calculate how many stuffed animals Jake sold
    jake = x + 10

    # Calculate how many more stuffed animals Quincy sold than Jake
    difference = quincy - jake

    result = difference
    return result

print(solution())