def solution():
    """Maggie has an after-school job that pays her $5.00 for every magazine subscription she can sell. She sells 4 to her parents, 1 to her grandfather, 2 to the next-door neighbor and twice that amount to another neighbor. How much money did Maggie earn?"""
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