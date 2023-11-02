def solution():
    ducks_bought = 30
    cost_per_duck = 10
    duck_weight = 4
    selling_price = 5
    total_weight = ducks_bought * duck_weight
    total_selling_price = total_weight * selling_price
    total_cost = ducks_bought * cost_per_duck
    profit = total_selling_price - total_cost
    result = profit
    return result

print(solution())