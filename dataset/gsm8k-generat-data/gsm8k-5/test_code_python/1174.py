def solution():
    total_butterflies = 11  # Martha has 11 butterflies in total
    black_butterflies = 5  # Martha has 5 black butterflies
    yellow_butterflies = (total_butterflies - black_butterflies) / 3  # Martha has 1/3rd of non-black butterflies as yellow butterflies
    blue_butterflies = 2 * yellow_butterflies  # Martha has twice as many blue butterflies as yellow butterflies
    result = blue_butterflies
    return result

print(solution())