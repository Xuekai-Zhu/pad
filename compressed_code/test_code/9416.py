def solution():
    
    price_per_subscription = 5
    subscriptions_to_parents = 4
    subscriptions_to_grandfather = 1
    subscriptions_to_neighbor_1 = 2
    subscriptions_to_neighbor_2 = subscriptions_to_neighbor_1 * 2
    total_subscriptions = subscriptions_to_parents + subscriptions_to_grandfather + subscriptions_to_neighbor_1 + subscriptions_to_neighbor_2
    money_earned = total_subscriptions * price_per_subscription
    result = money_earned
    return result

print(solution())