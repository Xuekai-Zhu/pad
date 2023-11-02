def solution():
    # Define the number of black butterflies
    black_butterflies = 5

    # Calculate the number of yellow butterflies
    yellow_butterflies = (11 - black_butterflies) / 3

    # Calculate the number of blue butterflies
    blue_butterflies = 2 * yellow_butterflies

    result = blue_butterflies
    return result

print(solution())