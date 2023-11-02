def solution():
    # Calculate the total revenue from selling slices
    slices_sold = 24
    slice_price = 3
    slices_revenue = slices_sold * slice_price

    # Calculate the total revenue from selling whole pizzas
    pizzas_sold = 3
    pizza_price = 15
    pizzas_revenue = pizzas_sold * pizza_price

    # Calculate the total revenue earned
    total_revenue = slices_revenue + pizzas_revenue
    result = total_revenue
    return result

print(solution())