def solution():
    small_pizza_price = 2  # Small pizza costs $2
    large_pizza_price = 8  # Large pizza costs $8
    total_pizza_sales = 40  # They sold $40 in pizzas
    num_small_pizzas = 8  # They sold 8 small pizzas

    # Calculate the total sales from large pizzas
    total_large_pizza_sales = total_pizza_sales - (num_small_pizzas * small_pizza_price)

    # Calculate the number of large pizzas sold
    num_large_pizzas = total_large_pizza_sales / large_pizza_price
    result = num_large_pizzas
    return result

print(solution())