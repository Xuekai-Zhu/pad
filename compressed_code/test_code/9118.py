def solution():
    
    slices_per_pizza = 8
    num_pizzas = 2
    slices_eaten = 7
    total_slices = slices_per_pizza * num_pizzas
    remaining_slices = total_slices - slices_eaten
    result = remaining_slices
    return result

print(solution())