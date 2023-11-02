def solution():
    """Piazzanos Pizzeria has a buy-1-get-1-free special on triple cheese pizzas, and a buy-2-get-1-free special on meat lovers pizzas. If the standard price for a pizza is $5, how much does it cost, in dollars, to purchase 10 triple cheese and 9 meat lovers pizzas using the special pricing?"""
    # Define the price of a standard pizza
    PRICE = 5

    # Define the number of pizzas purchased
    TRIPLE_CHEESE_PIZZAS = 10
    MEAT_LOVERS_PIZZAS = 9

    # Calculate the total price of the triple cheese pizzas with the buy-1-get-1-free special
    triple_cheese_price = (TRIPLE_CHEESE_PIZZAS // 2 + TRIPLE_CHEESE_PIZZAS % 2) * PRICE

    # Calculate the total price of the meat lovers pizzas with the buy-2-get-1-free special
    meat_lovers_price = ((MEAT_LOVERS_PIZZAS // 3) * 2 + MEAT_LOVERS_PIZZAS % 3) * PRICE

    # Calculate the total price of all the pizzas
    total_price = triple_cheese_price + meat_lovers_price

    result = total_price
    return result

print(solution())