def solution():
    """Ben has two brothers. They can each eat 12 slices of pizza. They are ordering pizza for the night and want to make sure they get enough. The large pizzas have 14 slices and the small pizzas have 8. If they order 1 small pizza, how many large pizzas do they need to order?"""
    total_slices_needed = 2 * 12 * 3  # 2 brothers * 12 slices * 3 pizzas
    small_pizza_slices = 8
    large_pizza_slices = 14
    slices_from_small_pizza = 1 * small_pizza_slices
    slices_from_large_pizzas = total_slices_needed - slices_from_small_pizza
    large_pizzas_needed = slices_from_large_pizzas // large_pizza_slices
    if slices_from_large_pizzas % large_pizza_slices != 0:
        large_pizzas_needed += 1

    result = large_pizzas_needed
    return result

print(solution())