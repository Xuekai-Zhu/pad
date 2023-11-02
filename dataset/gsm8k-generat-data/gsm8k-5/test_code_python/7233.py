def solution():
    total_butterflies = 19  # Martha has 19 butterflies in total
    blue_butterflies = 6  # Martha has 6 blue butterflies
    yellow_butterflies = blue_butterflies / 2  # Martha has twice as many blue butterflies as yellow butterflies
    black_butterflies = total_butterflies - blue_butterflies - yellow_butterflies  # The rest of Martha's butterflies are black
    result = black_butterflies
    return result

print(solution())