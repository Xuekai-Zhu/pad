def solution():
    """John's cow weighs 400 pounds. It increased its weight to 1.5 times its starting weight. He is able to sell the cow for $3 per pound. How much more is it worth after gaining the weight?"""
    starting_weight = 400
    weight_increase = 1.5
    current_weight = starting_weight * weight_increase
    price_per_pound = 3
    initial_worth = starting_weight * price_per_pound
    new_worth = current_weight * price_per_pound
    profit = new_worth - initial_worth
    result = profit
    return result

print(solution())