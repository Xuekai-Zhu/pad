def solution():
    cost_basic = 8
    cost_scientific = 2 * cost_basic
    cost_graphing = 3 * cost_scientific
    total_cost = cost_basic + cost_scientific + cost_graphing
    money_given = 100
    change = money_given - total_cost
    result = change
    return result

print(solution())