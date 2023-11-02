def solution():
    """In January, Bill's labrador puppy weighs 40 pounds and his dachshund puppy weighs 12 pounds. Each dog gains 25% of their starting weight over the year. What's the difference in their weight at the end of the year?"""
    labrador_start_weight = 40
    dachshund_start_weight = 12
    weight_gain_percent = 25
    weight_gain_multiplier = 1 + (weight_gain_percent / 100)
    labrador_end_weight = labrador_start_weight * weight_gain_multiplier
    dachshund_end_weight = dachshund_start_weight * weight_gain_multiplier
    weight_difference = labrador_end_weight - dachshund_end_weight
    result = weight_difference
    return result

print(solution())