def solution():
    
    apples_cost = 2 * 2
    pie_crust_cost = 2
    lemon_cost = 0.5
    butter_cost = 1.5
    total_cost = apples_cost + pie_crust_cost + lemon_cost + butter_cost
    cost_per_serving = total_cost / 8
    result = cost_per_serving
    
    return result

print(solution())