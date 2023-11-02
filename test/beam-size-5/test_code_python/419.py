def solution():
    
    tattered_jeans_cost = 28
    jogger_jeans_cost = tattered_jeans_cost - 6
    total_savings = 6
    tattered_jeans_total = tattered_jeans_cost / 3
    jogger_jeans_total = tattered_jeans_total + jogger_jeans_cost
    difference = jogger_jeans_total - tattered_jeans_total
    result = difference
    return result

print(solution())