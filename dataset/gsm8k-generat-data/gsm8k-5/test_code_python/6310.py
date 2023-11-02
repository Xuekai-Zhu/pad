def solution():
    # Find the weight of Jake
    jake_weight = 52 + 8

    # Find the weight of John
    john_weight = 158 - (52 + jake_weight)

    # Find the range of their weights
    weight_range = (min(52, jake_weight, john_weight), max(52, jake_weight, john_weight))

    result = weight_range
    return result

print(solution())