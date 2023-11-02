def solution():
    # Calculate the cost per slice of pizza
    cost_per_pizza = 72 / 3  # each pizza costs $72 and Kim buys 3 pizzas
    cost_per_slice = cost_per_pizza / 12  # each pizza has 12 slices
    cost_for_5_slices = cost_per_slice * 5  
    result = round(cost_for_5_slices, 2)  # Round the cost to 2 decimal places
    return result

print(solution())