def solution():
    cost1 = 13
    cost2 = 24
    remaining_budget = 6
    new_budget = 50

    total_cost = cost1 + cost2
    total_budget = remaining_budget + new_budget

    remaining_money = total_budget - total_cost
    result = remaining_money
    return result

print(solution())