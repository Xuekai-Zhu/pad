def solution():
    """John's cow weighs 400 pounds. It increased its weight to 1.5 times its starting weight. He is able to sell the cow for $3 per pound. How much more is it worth after gaining the weight?"""
    starting_weight = 400
    increased_weight = starting_weight * 1.5
    price_per_pound = 3
    starting_value = starting_weight * price_per_pound
    increased_value = increased_weight * price_per_pound
    difference = increased_value - starting_value
    result = difference
    return result

print(solution())