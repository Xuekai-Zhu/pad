def solution():
    """John's weight bench can support 1000 pounds. He wants to make sure to stay 20% under that weight for safety. If he weighs 250 pounds how much weight can he put on the bar?"""
    weight_limit = 1000 * 0.8
    john_weight = 250
    max_weight = weight_limit - john_weight
    result = max_weight
    return result

print(solution())