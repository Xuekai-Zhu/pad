def solution():
    # Calculate the number of brown toads per acre
    spotted_brown_toads = 50
    brown_toads = 4 * spotted_brown_toads
    total_toads = brown_toads + 1 * brown_toads / 25

    # Calculate the number of green toads per acre
    green_toads = total_toads / 26

    result = green_toads
    return result

print(solution())