def solution():
    
    pizza_cost = 10
    num_slices = 8
    num_toppings = 7
    topping_cost = 2 + 1 + 1 + (num_toppings - 3) * 0.5
    total_cost = pizza_cost + topping_cost
    cost_per_slice = total_cost / num_slices
    result = cost_per_slice
    return result

print(solution())