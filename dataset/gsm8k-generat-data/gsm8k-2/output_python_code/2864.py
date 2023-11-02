def solution():
    """There were 25 peaches in each basket. Five baskets of peaches were delivered to a market. The farmers have eaten 5 peaches. The remaining peaches are packed into smaller boxes of 15 each. How many boxes of peaches are there?"""
    peaches_per_basket = 25
    num_baskets = 5
    total_peaches = peaches_per_basket * num_baskets
    eaten_peaches = 5
    remaining_peaches = total_peaches - eaten_peaches
    boxes_of_peaches = remaining_peaches // 15
    result = boxes_of_peaches
    return result

print(solution())