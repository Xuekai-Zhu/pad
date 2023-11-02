def solution():
    cost_per_dozen = 6
    roses_bought = 5
    total_cost = cost_per_dozen * roses_bought
    discount = 20
    final_cost = total_cost - ((discount / 100) * total_cost)
    result = final_cost
    return result

print(solution())