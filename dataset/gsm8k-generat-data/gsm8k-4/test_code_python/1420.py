def solution():
    """Compared to the amount of water she drank, Carla drank three times as much soda minus 6 ounces. If she drank 54 ounces of liquid total, how much water did she drink?"""
    # Let x be the amount of water Carla drank, then the amount of soda she drank is 3x-6
    # We know that the total amount of liquid she drank is 54, so:
    x + (3x-6) = 54

    # Simplify and solve for x
    4x - 6 = 54
    4x = 60
    x = 15

    # The amount of water Carla drank is x = 15 ounces
    result = x
    return result

print(solution())