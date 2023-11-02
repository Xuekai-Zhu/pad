def solution():
    """The cost of transporting 80 bags of cement, each weighing 50 kgs, is $6000. What's the cost of transporting three times as many cement bags, each weighing 3/5 times as many kgs?"""
    bags = 80
    weight_per_bag = 50
    cost = 6000
    new_bags = 3 * bags
    new_weight_per_bag = (3/5) * weight_per_bag
    new_cost = (new_bags * new_weight_per_bag * cost) / (bags * weight_per_bag)
    result = new_cost
    return result

print(solution())