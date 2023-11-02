def solution():
    """A small pizza has 6 slices, a medium pizza has 8 slices whereas a large pizza has 12 slices. How many slices of pizza will you have if you bought a total of 15 pizzas and you know you ordered 4 small pizzas and 5 medium pizzas?"""
    small_pizza_slices = 6
    medium_pizza_slices = 8
    large_pizza_slices = 12
    total_small_pizzas = 4
    total_medium_pizzas = 5
    total_large_pizzas = 15 - total_small_pizzas - total_medium_pizzas
    total_slices = (small_pizza_slices * total_small_pizzas) + (medium_pizza_slices * total_medium_pizzas) + (large_pizza_slices * total_large_pizzas)
    result = total_slices
    return result

print(solution())