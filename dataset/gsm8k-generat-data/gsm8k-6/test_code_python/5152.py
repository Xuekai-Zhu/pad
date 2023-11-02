def solution():
    # Calculate the total cost of the pizza with all toppings
    cost_pizza = 10 + 2 + 2 + 1 + 1 + 0.5 + 0.5 + 0.5 # large pizza costs $10, first topping costs $2, next 2 toppings cost $1 each, rest of the toppings cost $0.50 each
    
    # Calculate the cost per slice
    slices = 8  # a large pizza is cut into 8 slices
    cost_per_slice = cost_pizza / slices
    
    result = cost_per_slice
    return result

print(solution())