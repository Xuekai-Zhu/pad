def solution():
    """Martin's weight is 55 kg. Carl’s weight is 16 kg more than Martin’s weight. Christian’s weight is 8 kg more than Carl’s weight. Harry is 5 kg less than Christian’s weight. What is the weight of Harry, in kg?"""
    martin_weight = 55
    carl_weight = martin_weight + 16
    christian_weight = carl_weight + 8
    harry_weight = christian_weight - 5
    result = harry_weight
    return result

print(solution())