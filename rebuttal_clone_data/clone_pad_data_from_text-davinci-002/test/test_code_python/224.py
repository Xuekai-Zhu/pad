def solution():
    adult_weight = 140
    child_weight = 64
    total_weight = adult_weight * 3 + child_weight * 2
    max_weight = 600 - total_weight
    result = max_weight
    return result

print(solution())