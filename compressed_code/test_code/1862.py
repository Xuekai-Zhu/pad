def solution():
    
    num_days = 2
    amulets_per_day = 25
    sale_price = 40
    cost_price = 30
    faire_percent = 0.1

    total_sales = num_days * amulets_per_day * sale_price
    total_cost = num_days * amulets_per_day * cost_price
    faire_cut = total_sales * faire_percent
    profit = total_sales - total_cost - faire_cut
    result = profit
    return result

print(solution())