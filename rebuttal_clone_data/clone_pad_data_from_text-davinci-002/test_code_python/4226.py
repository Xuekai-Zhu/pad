def solution():
    slices_in_pizza = 8
    pizzas_ordered = 2
    slices_eaten = 7
    slices_leftover = slices_in_pizza * pizzas_ordered - slices_eaten
    result = slices_leftover
    return result

print(solution())