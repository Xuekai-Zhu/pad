def solution():
    # Define the number of blue butterflies and yellow butterflies
    blue_butterflies = 6
    yellow_butterflies = blue_butterflies / 2  # Since there are twice as many blue as yellow

    # Calculate the total number of black butterflies
    total_black_butterflies = 19 - blue_butterflies - yellow_butterflies

    result = total_black_butterflies
    return result

print(solution())