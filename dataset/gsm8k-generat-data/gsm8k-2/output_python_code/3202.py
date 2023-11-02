def solution():
    """The cost of transporting 80 bags of cement, each weighing 50 kgs, is $6000. What's the cost of transporting three times as many cement bags, each weighing 3/5 times as many kgs?"""
    original_bags = 80
    original_weight = 50
    original_cost = 6000
    new_bags = 240
    new_weight = 3/5 * original_weight
    new_cost = (new_bags * new_weight * original_cost) / (original_bags * original_weight)
    result = new_cost
    return result

print(solution())