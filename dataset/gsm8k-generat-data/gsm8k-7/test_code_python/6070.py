def solution():
    num_pizzas = 4
    total_cost = 80
    num_slices_per_pizza = 5

    # Calculate the total number of pizza slices
    total_slices = num_pizzas * num_slices_per_pizza

    # Calculate the cost per pizza slice
    cost_per_slice = total_cost / total_slices

    result = cost_per_slice
    return result

print(solution())