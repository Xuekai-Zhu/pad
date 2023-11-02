def solution():
    slices_per_pizza = 8
    num_pizzas = 2
    slices_eaten = 7

    # Calculate the total number of slices in both pizzas
    total_slices = slices_per_pizza * num_pizzas

    # Calculate the remaining slices after Mary eats 7
    remaining_slices = total_slices - slices_eaten
    result = remaining_slices
    return result

print(solution())