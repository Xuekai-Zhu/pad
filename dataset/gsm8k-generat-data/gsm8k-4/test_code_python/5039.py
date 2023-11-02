def solution():
    """The pizzeria sells small pizzas for $2 and large pizzas for $8. They sold $40 in pizzas. If they sold 8 small pizzas, how many large pizzas did they sell?"""
    # Define the price of a small pizza and a large pizza
    SMALL_PIZZA_PRICE = 2
    LARGE_PIZZA_PRICE = 8

    # Define the total sales and the number of small pizzas sold
    total_sales = 40
    small_pizzas_sold = 8

    # Calculate the total sales from large pizzas
    large_pizza_sales = total_sales - (small_pizzas_sold * SMALL_PIZZA_PRICE)

    # Calculate the number of large pizzas sold
    large_pizzas_sold = large_pizza_sales / LARGE_PIZZA_PRICE

    # Round the number of large pizzas sold to the nearest whole number
    large_pizzas_sold = round(large_pizzas_sold)

    result = large_pizzas_sold
    return result

print(solution())