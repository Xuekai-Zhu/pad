def solution():
    small_pizza_price = 2
    large_pizza_price = 8
    total_sales = 40
    num_small_pizzas = 8

    # Calculate the total sales from only small pizzas
    small_pizza_sales = num_small_pizzas * small_pizza_price

    # Calculate the total sales from only large pizzas
    large_pizza_sales = total_sales - small_pizza_sales

    # Calculate the number of large pizzas sold
    num_large_pizzas = large_pizza_sales / large_pizza_price
    result = num_large_pizzas
    return result

print(solution())