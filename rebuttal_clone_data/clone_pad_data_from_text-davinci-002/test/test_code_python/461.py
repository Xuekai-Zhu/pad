def solution():
    cost_cappuccino = 2
    cost_iced_tea = 3
    cost_cafe_latte = 1.5
    cost_espresso = 1
    total_cost = cost_cappuccino * 3 + cost_iced_tea * 2 + cost_cafe_latte * 2 + cost_espresso * 2
    change = 20 - total_cost
    result = change
    return result

print(solution())