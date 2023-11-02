def solution():
    """John's cow weighs 400 pounds. It increased its weight to 1.5 times its starting weight. He is able to sell the cow for $3 per pound. How much more is it worth after gaining the weight?"""
    initial_weight = 400
    increase_factor = 1.5
    increased_weight = initial_weight * increase_factor
    price_per_pound = 3
    increased_value = increased_weight * price_per_pound
    result = increased_value - (initial_weight * price_per_pound)
    return result

print(solution())