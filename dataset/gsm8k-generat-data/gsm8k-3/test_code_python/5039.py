def solution():
    """The pizzeria sells small pizzas for $2 and large pizzas for $8. They sold $40 in pizzas. If they sold 8 small pizzas, how many large pizzas did they sell?"""
    # Define the price of a small pizza and a large pizza
    SMALL_PRICE = 2
    LARGE_PRICE = 8

    # Define the total sales and the number of small pizzas sold
    total_sales = 40
    num_small_pizzas = 8

    # Calculate the total sales from the large pizzas
    large_sales = total_sales - (num_small_pizzas * SMALL_PRICE)

    # Calculate the number of large pizzas sold
    num_large_pizzas = large_sales / LARGE_PRICE

    # Display the number of large pizzas sold
    result = num_large_pizzas
    return result

print(solution())