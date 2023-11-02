def solution():
    """Maggie has an after-school job that pays her $5.00 for every magazine subscription she can sell. She sells 4 to her parents, 1 to her grandfather, 2 to the next-door neighbor and twice that amount to another neighbor. How much money did Maggie earn?"""
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