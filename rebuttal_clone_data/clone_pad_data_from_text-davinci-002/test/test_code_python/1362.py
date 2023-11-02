def solution():
    cost_per_pineapple = 1.25
    pineapples_bought = 12
    shipping_cost = 21.00
    total_cost = cost_per_pineapple * pineapples_bought + shipping_cost
    cost_per_pineapple_shipped = total_cost / pineapples_bought
    result = cost_per_pineapple_shipped
    return result

print(solution())