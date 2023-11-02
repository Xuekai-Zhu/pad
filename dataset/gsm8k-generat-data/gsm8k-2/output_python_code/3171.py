def solution():
    """Three friends agreed to pay an equal amount of money for buying 5 bags of chips. If they each pay $5, how much does each bag of chips cost?"""
    num_friends = 3
    total_cost = num_friends * 5
    num_bags = 5
    cost_per_bag = total_cost / num_bags
    result = cost_per_bag
    return result

print(solution())