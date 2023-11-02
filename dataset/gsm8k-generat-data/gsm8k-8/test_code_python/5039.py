def solution():
    # Define the price and quantity of each pizza size
    small_pizza_price = 2
    large_pizza_price = 8
    small_pizza_quantity = 8

    # Calculate the total revenue from small pizzas
    small_pizza_revenue = small_pizza_price * small_pizza_quantity

    # Calculate the total revenue from all pizzas
    total_revenue = 40

    # Calculate the revenue from the large pizzas
    large_pizza_revenue = total_revenue - small_pizza_revenue

    # Calculate the quantity of large pizzas sold
    large_pizza_quantity = large_pizza_revenue / large_pizza_price

    result = large_pizza_quantity
    return result

print(solution())