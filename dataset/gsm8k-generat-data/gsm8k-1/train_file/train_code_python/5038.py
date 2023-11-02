def solution():
    """The pizzeria sells small pizzas for $2 and large pizzas for $8. They sold $40 in pizzas. If they sold 8 small pizzas, how many large pizzas did they sell?"""
    small_price = 2
    large_price = 8
    total_sales = 40
    small_sales = 8 * small_price
    large_sales = total_sales - small_sales
    num_large_pizzas = large_sales / large_price
    result = num_large_pizzas
    return result

print(solution())