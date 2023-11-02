def solution():
    
    pool_fill_time = 50
    hose_rate = 100
    total_gallons = pool_fill_time * hose_rate
    cost_per_gallon = 0.1
    total_cost = (total_gallons * cost_per_gallon) / 100
    result = total_cost
    return result

print(solution())