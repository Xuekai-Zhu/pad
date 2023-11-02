def solution():
    """Terry's mom brought home 4 different colored dogs from the shelter. The brown dog weighs 4 pounds. The black dog weighs 1 pound more than the brown dog. The white dog weighs twice as much as the brown dog. The grey dog weighs 2 pounds less than the black dog. What's the average weight of all the dogs?"""
    brown_weight = 4
    black_weight = brown_weight + 1
    white_weight = brown_weight * 2
    grey_weight = black_weight - 2
    total_weight = brown_weight + black_weight + white_weight + grey_weight
    average_weight = total_weight / 4
    result = average_weight
    return result

print(solution())