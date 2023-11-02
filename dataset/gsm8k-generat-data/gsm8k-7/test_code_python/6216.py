def solution():
    original_budget = X # insert original gym budget (in dollars)
    increase_percentage = 0.20 # 20% increase
    new_budget = original_budget * (1 + increase_percentage)

    softball_price = 9
    num_softballs = int(new_budget / softball_price)

    result = num_softballs
    return result

print(solution())