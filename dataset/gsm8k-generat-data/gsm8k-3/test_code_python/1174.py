def solution():
    """Martha has 11 butterflies in her collection. She has twice as many blue butterflies as yellow butterflies. The rest of her butterflies are black. If Martha has 5 black butterflies, how many blue butterflies does she have?"""
    # Define the number of black butterflies
    black_butterflies = 5

    # Calculate the number of yellow butterflies
    yellow_butterflies = (11 - black_butterflies) / 3

    # Calculate the number of blue butterflies
    blue_butterflies = 2 * yellow_butterflies

    # Display the number of blue butterflies
    result = blue_butterflies
    return result

print(solution())