def solution():
    tracy_weight = 52
    jake_weight = tracy_weight + 8
    john_weight = 158 - (tracy_weight + jake_weight)
    weights = [tracy_weight, jake_weight, john_weight]
    max_weight = max(weights)
    min_weight = min(weights)
    result = (min_weight, max_weight)
    return result

print(solution())