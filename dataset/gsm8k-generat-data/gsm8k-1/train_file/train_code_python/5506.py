def solution():
    """John's weight bench can support 1000 pounds. He wants to make sure to stay 20% under that weight for safety. If he weighs 250 pounds how much weight can he put on the bar?"""
    max_weight = 1000 * 0.8  # staying 20% under the limit
    weight_allowed = max_weight - 250  # subtracting John's weight from the max weight allowed
    result = weight_allowed
    return result

print(solution())