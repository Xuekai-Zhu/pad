def solution():
    
    small_pizza_slices = 6
    medium_pizza_slices = 8
    large_pizza_slices = 12
    total_pizzas = 15
    small_pizzas_ordered = 4
    medium_pizzas_ordered = 5
    large_pizzas_ordered = total_pizzas - small_pizzas_ordered - medium_pizzas_ordered
    total_slices = (small_pizzas_ordered * small_pizza_slices) + (medium_pizzas_ordered * medium_pizza_slices) + (large_pizzas_ordered * large_pizza_slices)
    result = total_slices
    return result

print(solution())