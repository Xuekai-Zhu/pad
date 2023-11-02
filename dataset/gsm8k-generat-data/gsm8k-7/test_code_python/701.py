def solution():
    num_pizzas = 3
    num_slices_per_pizza = 12
    total_slices = num_pizzas * num_slices_per_pizza
    total_cost = 72
    cost_per_slice = total_cost / total_slices
    num_slices_wanted = 5
    cost_of_5_slices = cost_per_slice * num_slices_wanted
    result = cost_of_5_slices
    return result

print(solution())