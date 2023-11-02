def solution():
    """Martha has 19 butterflies in her collection. She has twice as many blue butterflies as yellow butterflies. The rest of her butterflies are black. If Martha has 6 blue butterflies, how many black butterflies does she have?"""
    
    # Let's represent the number of yellow butterflies as y.
    # Since she has twice as many blue butterflies as yellow butterflies, the number of blue butterflies is 2y.
    # The total number of butterflies is 19, so the number of black butterflies is 19 - (y + 2y) = 19 - 3y.
    # We know that Martha has 6 blue butterflies, so 2y = 6 and y = 3.
    # Therefore, the number of black butterflies is 19 - 3y = 19 - 9 = 10.
    
    # Display the number of black butterflies
    result = 10
    return result

print(solution())