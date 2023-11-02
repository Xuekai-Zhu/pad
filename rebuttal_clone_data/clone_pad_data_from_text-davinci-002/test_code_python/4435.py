def solution():
    total_cost = 25
    cost_milk = 3
    cost_cereal = 7
    cost_bananas = 1
    cost_apples = 2
    cost_cookies = (total_cost - cost_milk - cost_cereal - cost_bananas - cost_apples) / 2
    result = cost_cookies
    return result

print(solution())