def solution():
    """Tracy, John and Jake found their combined weight to be 158 kilograms. If Tracy weighs 52 kg and Jake weighs 8kg more than Tracy, what is the range of their weights?"""
    tracy_weight = 52
    jake_weight = tracy_weight + 8
    john_weight = 158 - tracy_weight - jake_weight
    min_weight = min(tracy_weight, jake_weight, john_weight)
    max_weight = max(tracy_weight, jake_weight, john_weight)
    result = (min_weight, max_weight)
    return result

print(solution())