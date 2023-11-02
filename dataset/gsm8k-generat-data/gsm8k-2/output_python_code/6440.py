def solution():
    """Jaco wants to buy Christmas gifts for his 8 friends that are worth $9 each. Also, he wants to buy gifts for his mother and father that are of the same amount. He has a $100 budget to buy all gifts. How much is Jaco's budget for each of his mother and father's gift?"""
    num_friends = 8
    friend_gift_price = 9
    friend_gift_total_cost = num_friends * friend_gift_price
    total_budget = 100
    parents_gift_total_cost = total_budget - friend_gift_total_cost
    num_parents = 2
    parents_gift_price = parents_gift_total_cost / num_parents
    result = parents_gift_price
    return result

print(solution())