def solution():
    sandwich_cost = 0.30  # Cost of one sandwich
    juice_cost = 0.20  # Cost of one pack of juice
    total_cost = sandwich_cost + juice_cost  # Total cost of one meal

    lyle_budget = 2.50  # Lyle has $2.50 to spend
    max_friends = int(lyle_budget / total_cost) - 1  # Lyle wants to buy for himself and his friends, so he can buy for one less friend

    result = max_friends
    return result

print(solution())