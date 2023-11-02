def solution():
    
    sandwich_cost = 4
    juice_cost = 2 * sandwich_cost
    total_cost = sandwich_cost + juice_cost
    milk_cost = 0.75 * total_cost
    total_food_cost = milk_cost + total_cost
    result = total_food_cost
    return result

print(solution())