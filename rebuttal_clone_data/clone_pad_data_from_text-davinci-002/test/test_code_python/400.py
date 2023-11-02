def solution():
    pizzas_bought = 3
    slices_per_pizza = 12
    total_cost = 72
    cost_per_slice = total_cost / (pizzas_bought * slices_per_pizza)
    result = cost_per_slice * 5
    return result

print(solution())