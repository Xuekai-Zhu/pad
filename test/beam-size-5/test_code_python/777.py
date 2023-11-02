def solution():
    
    total_pizzas = 4
    total_cost = 64
    cost_of_two_pizzas = 30
    cost_of_other_pizzas = (total_cost - cost_of_two_pizzas) / 2
    result = cost_of_other_pizzas
    return result

print(solution())