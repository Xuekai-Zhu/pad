def solution():
    brown_weight = 4
    black_weight = brown_weight + 1
    white_weight = brown_weight * 2
    grey_weight = black_weight - 2

    # Calculate the sum of all the dogs' weights
    total_weight = brown_weight + black_weight + white_weight + grey_weight

    # Calculate the average weight of all the dogs
    average_weight = total_weight / 4
    result = average_weight
    return result

print(solution())