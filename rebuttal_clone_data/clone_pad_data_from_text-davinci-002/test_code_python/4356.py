def solution():
    total_pizzas = 15
    small_pizza_slices = 6
    medium_pizza_slices = 8
    large_pizza_slices = 12
    small_pizzas = 4
    medium_pizzas = 5
    large_pizzas = total_pizzas - (small_pizzas + medium_pizzas)
    total_slices = (small_pizza_slices * small_pizzas) + (medium_pizza_slices * medium_pizzas) + (large_pizza_slices * large_pizzas)
    result = total_slices
    return result

print(solution())