def solution():
    """Susie opens a pizza store. She charges $3 per slice and $15 for a whole pizza. If she was able to sell 24 slices of pizza and 3 whole pizzas, how much money did she earn?"""
    slices_sold = 24
    pizzas_sold = 3
    price_per_slice = 3
    price_per_pizza = 15
    total_slices = slices_sold + (pizzas_sold * 8)  # each pizza has 8 slices
    total_sales = (slices_sold * price_per_slice) + (pizzas_sold * price_per_pizza)
    result = total_sales
    return result

print(solution())