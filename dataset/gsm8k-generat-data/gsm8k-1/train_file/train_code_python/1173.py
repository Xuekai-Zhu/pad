def solution():
    """Martha has 11 butterflies in her collection. She has twice as many blue butterflies as yellow butterflies. The rest of her butterflies are black. If Martha has 5 black butterflies, how many blue butterflies does she have?"""
    total_butterflies = 11
    black_butterflies = 5
    yellow_butterflies = (total_butterflies - black_butterflies) / 3
    blue_butterflies = 2 * yellow_butterflies
    result = blue_butterflies
    return result

print(solution())