def solution():
    """The pizzeria sells small pizzas for $2 and large pizzas for $8. They sold $40 in pizzas. If they sold 8 small pizzas, how many large pizzas did they sell?"""
    small_price = 2
    large_price = 8
    total_price = 40
    num_small = 8
    total_num_pizzas = total_price / small_price
    num_large = (total_num_pizzas - num_small) / (large_price - small_price)
    result = num_large
    return result

print(solution())