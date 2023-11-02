def solution():
    # Find the number of yellow houses
    yellow_houses = 90 / 3  # Isabella has three times as many green houses as yellow houses
    # Find the number of red houses
    red_houses = yellow_houses + 40  # Isabella has 40 fewer yellow houses than red houses
    # Find the total number of non-yellow houses
    non_yellow_houses = green_houses + red_houses
    result = non_yellow_houses
    return result

print(solution())