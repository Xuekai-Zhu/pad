def solution():
    """Ben has two brothers. They can each eat 12 slices of pizza. They are ordering pizza for the night and want to make sure they get enough. The large pizzas have 14 slices and the small pizzas have 8. If they order 1 small pizza, how many large pizzas do they need to order?"""
    slices_per_person = 12
    small_pizza_slices = 8
    large_pizza_slices = 14
    total_slices_needed = (slices_per_person * 3) - small_pizza_slices
    large_pizzas_needed = total_slices_needed // large_pizza_slices + \
        (1 if total_slices_needed %
         large_pizza_slices != 0 else 0)  # ceiling division
    result = large_pizzas_needed
    return result

print(solution())