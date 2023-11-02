def solution():
    slices_per_pizza = 8  # Each large pizza has 8 slices
    total_pizzas = 2  # Mary orders 2 large pizzas
    slices_eaten = 7  # Mary eats 7 slices

    # Calculate the total number of slices
    total_slices = slices_per_pizza * total_pizzas

    # Calculate the remaining slices
    remaining_slices = total_slices - slices_eaten
    result = remaining_slices
    return result

print(solution())