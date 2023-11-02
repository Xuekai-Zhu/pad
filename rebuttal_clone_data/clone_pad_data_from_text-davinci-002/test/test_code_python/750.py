def solution():
    pizzas_ordered = 2
    slices_per_pizza = 6
    total_slices = pizzas_ordered * slices_per_pizza
    slices_eaten = total_slices * 2/3
    result = slices_eaten
    return result

print(solution())