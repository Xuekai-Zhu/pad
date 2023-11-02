def solution():
    """Susie opens a pizza store. She charges $3 per slice and $15 for a whole pizza. If she was able to sell 24 slices of pizza and 3 whole pizzas, how much money did she earn?"""
    slice_price = 3
    pizza_price = 15
    slices_sold = 24
    pizzas_sold = 3
    total_sales = (slice_price * slices_sold) + (pizza_price * pizzas_sold)
    result = total_sales
    return result

print(solution())