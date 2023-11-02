def solution():
    cost_per_apple = 2
    cost_per_orange = 1.50
    apples_bought = 10
    oranges_bought = 5
    cheaper_fruit = "apples"
    
    if cost_per_orange < cost_per_apple:
        cheaper_fruit = "oranges"
    
    if cheaper_fruit == "apples":
        total_cost = cost_per_apple * apples_bought
    else:
        total_cost = cost_per_orange * oranges_bought
    
    result = total_cost
    return result

print(solution())