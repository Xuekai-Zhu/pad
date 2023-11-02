def solution():
    small_pizza_slices = 6
    medium_pizza_slices = 8
    large_pizza_slices = 12
    total_small_pizzas = 4
    total_medium_pizzas = 5
    total_large_pizzas = 15 - total_small_pizzas - total_medium_pizzas
    
    # Calculate the total number of pizza slices
    total_slices = (total_small_pizzas * small_pizza_slices) + (total_medium_pizzas * medium_pizza_slices) + (total_large_pizzas * large_pizza_slices)
    result = total_slices
    return result

print(solution())