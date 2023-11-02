def solution():
    """Martha has 11 butterflies in her collection. She has twice as many blue butterflies as yellow butterflies. The rest of her butterflies are black. If Martha has 5 black butterflies, how many blue butterflies does she have?"""
    # Define the total number of butterflies
    total_butterflies = 11

    # Calculate the number of black butterflies
    black_butterflies = 5

    # Calculate the number of yellow butterflies
    yellow_butterflies = (total_butterflies - black_butterflies) / 3

    # Calculate the number of blue butterflies
    blue_butterflies = 2 * yellow_butterflies

    # return the result
    result = blue_butterflies
    return result

print(solution())