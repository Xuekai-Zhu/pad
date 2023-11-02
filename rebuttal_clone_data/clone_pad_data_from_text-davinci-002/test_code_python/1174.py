def solution():
    total_butterflies = 11
    black_butterflies = 5
    yellow_butterflies = (total_butterflies - black_butterflies) / 2
    blue_butterflies = total_butterflies - black_butterflies - yellow_butterflies
    result = blue_butterflies
    
    return result

print(solution())