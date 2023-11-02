def solution():
    standard_weight = 100
    min_weight = (standard_weight + 5) / 2  # minimum weight must be at least 5 pounds heavier than standard weight
    max_weight = 2 * min_weight  # maximum weight is twice the minimum weight
    result = max_weight
    return result

print(solution())