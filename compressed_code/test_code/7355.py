def solution():
    
    broccoli_cost = 3 * 4
    orange_cost = 3 * 0.75
    cabbage_cost = 3.75
    bacon_cost = 3
    chicken_cost = 2 * 3
    total_cost = broccoli_cost + orange_cost + cabbage_cost + bacon_cost + chicken_cost
    meat_cost = bacon_cost + chicken_cost
    percent_meat_cost = int((meat_cost / total_cost) * 100 + 0.5)
    result = percent_meat_cost
    return result

print(solution())