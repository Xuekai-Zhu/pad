def solution():
    num_large_pizzas = 2
    num_small_pizzas = 2
    num_slices_per_large_pizza = 16
    num_slices_per_small_pizza = 8

    # Calculate the total number of slices from the large pizzas
    total_large_slices = num_large_pizzas * num_slices_per_large_pizza

    # Calculate the total number of slices from the small pizzas
    total_small_slices = num_small_pizzas * num_slices_per_small_pizza

    # Calculate the total number of pizza slices that Albert eats
    total_slices_eaten = total_large_slices + total_small_slices
    result = total_slices_eaten
    return result

print(solution())