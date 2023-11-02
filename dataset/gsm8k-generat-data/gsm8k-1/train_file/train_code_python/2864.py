def solution():
    """There were 25 peaches in each basket. Five baskets of peaches were delivered to a market. The farmers have eaten 5 peaches. The remaining peaches are packed into smaller boxes of 15 each. How many boxes of peaches are there?"""
    peaches_per_basket = 25
    baskets_delivered = 5
    peaches_eaten = 5
    remaining_peaches = peaches_per_basket * baskets_delivered - peaches_eaten
    boxes_packed = remaining_peaches // 15
    result = boxes_packed
    return result

print(solution())