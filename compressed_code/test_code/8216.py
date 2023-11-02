def solution():
    
    brown_weight = 4
    black_weight = brown_weight + 1
    white_weight = brown_weight * 2
    grey_weight = black_weight - 2
    total_weight = brown_weight + black_weight + white_weight + grey_weight
    average_weight = total_weight / 4
    result = average_weight
    return result

print(solution())