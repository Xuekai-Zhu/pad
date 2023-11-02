def solution():
    # Calculate the ratio of spotted to gilled mushrooms
    ratio = 9 + 1

    # Calculate the number of spotted mushrooms
    spotted = 30 / ratio * 9

    # Calculate the number of gilled mushrooms
    gilled = 30 - spotted

    result = gilled
    return result

print(solution())