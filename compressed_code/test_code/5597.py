def solution():
    
    total_butterflies = 19
    blue_butterflies = 6
    yellow_butterflies = blue_butterflies / 2
    black_butterflies = total_butterflies - blue_butterflies - yellow_butterflies
    result = black_butterflies
    return result

print(solution())