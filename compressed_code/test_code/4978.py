def solution():
    
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