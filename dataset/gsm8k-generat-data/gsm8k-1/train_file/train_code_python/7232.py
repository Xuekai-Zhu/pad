def solution():
    """Martha has 19 butterflies in her collection. She has twice as many blue butterflies as yellow butterflies. The rest of her butterflies are black. If Martha has 6 blue butterflies, how many black butterflies does she have?"""
    total_butterflies = 19
    blue_butterflies = 6
    yellow_butterflies = blue_butterflies / 2
    black_butterflies = total_butterflies - blue_butterflies - yellow_butterflies
    result = black_butterflies
    return result

print(solution())