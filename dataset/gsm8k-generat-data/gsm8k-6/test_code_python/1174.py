def solution():
    # Calculate the number of yellow butterflies and blue butterflies
    yellow_butterflies = (11 - 5) // 3  # there are 5 black butterflies, so the remaining 6 butterflies are either yellow or blue
    blue_butterflies = 2 * yellow_butterflies  

    result = blue_butterflies
    return result

print(solution())