def solution():
    
    subscription_price = 5
    parents_subscriptions = 4
    grandfather_subscriptions = 1
    first_neighbor_subscriptions = 2
    second_neighbor_subscriptions = 2 * first_neighbor_subscriptions
    total_subscriptions = parents_subscriptions + grandfather_subscriptions + first_neighbor_subscriptions + second_neighbor_subscriptions
    total_earned = total_subscriptions * subscription_price
    result = total_earned
    return result

print(solution())