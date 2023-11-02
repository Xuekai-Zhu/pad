def solution():
    """Martha has 19 butterflies in her collection. She has twice as many blue butterflies as yellow butterflies.
    The rest of her butterflies are black. If Martha has 6 blue butterflies, how many black butterflies does she have?"""
    # Define the number of blue butterflies
    blue_butterflies = 6
    
    # Calculate the number of yellow butterflies
    yellow_butterflies = blue_butterflies / 2
    
    # Calculate the total number of blue and yellow butterflies
    colored_butterflies = blue_butterflies + yellow_butterflies
    
    # Calculate the number of black butterflies
    black_butterflies = 19 - colored_butterflies
    
    # return the result
    result = black_butterflies
    return result

print(solution())