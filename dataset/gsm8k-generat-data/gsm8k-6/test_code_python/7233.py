def solution():
    # Find the number of yellow butterflies
    yellow_butterflies = (19 - 6) / 3 # yellow butterflies are one third of the total butterflies

    # Find the number of black butterflies
    black_butterflies = 19 - 6 - yellow_butterflies

    result = black_butterflies
    return result

print(solution())