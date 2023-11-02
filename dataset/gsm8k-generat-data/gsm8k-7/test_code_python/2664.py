def solution():
    num_pizzas = 4
    slices_per_pizza = 12
    total_slices = num_pizzas * slices_per_pizza
    num_slices_eaten = 39

    # Calculate the number of slices remaining
    slices_remaining = total_slices - num_slices_eaten
    result = slices_remaining
    return result

print(solution())