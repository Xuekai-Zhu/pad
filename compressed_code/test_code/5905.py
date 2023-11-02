def solution():
    
    sandwich_cost = 4
    juice_cost = 2 * sandwich_cost
    total_cost_sandwich_juice = sandwich_cost + juice_cost
    milk_cost = 0.75 * total_cost_sandwich_juice
    total_cost = sandwich_cost + juice_cost + milk_cost
    return total_cost

print(solution())