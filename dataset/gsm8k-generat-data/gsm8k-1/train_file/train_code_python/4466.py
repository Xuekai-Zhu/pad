def solution():
    """Julie is making caesar salad for a family picnic. At the market, she spends $8 on green lettuce and $6 on red lettuce. If each type of lettuce costs $2 per pound, how many total pounds of lettuce did she buy?"""
    cost_per_pound = 2
    green_lettuce_cost = 8
    red_lettuce_cost = 6
    total_cost = green_lettuce_cost + red_lettuce_cost
    total_pounds = total_cost / cost_per_pound
    result = total_pounds
    return result

print(solution())