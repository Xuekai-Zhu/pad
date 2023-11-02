def solution():
    """A chef bought 4 bags of onions. Each bag weighs 50 pounds. A pound of onions cost $1.50. How much did the chef spend?"""
    bags_of_onions = 4
    weight_per_bag = 50
    price_per_pound = 1.5
    total_weight = bags_of_onions * weight_per_bag
    total_cost = total_weight * price_per_pound
    result = total_cost
    return result

print(solution())