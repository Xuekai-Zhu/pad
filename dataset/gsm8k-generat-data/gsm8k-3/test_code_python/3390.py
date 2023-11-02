def solution():
    """Piazzanos Pizzeria has a buy-1-get-1-free special on triple cheese pizzas, and a buy-2-get-1-free special on meat lovers pizzas.  If the standard price for a pizza is $5, how much does it cost, in dollars, to purchase 10 triple cheese and 9 meat lovers pizzas using the special pricing?"""
    # Define the prices and discounts for each type of pizza
    REGULAR_PRICE = 5
    CHEESE_DISCOUNT = 1/2
    MEAT_DISCOUNT = 2/3

    # Calculate the cost of the triple cheese pizzas with the buy-1-get-1-free special
    triple_cheese_cost = ((10/2) + (10 % 2)) * (REGULAR_PRICE * (1 - CHEESE_DISCOUNT))

    # Calculate the cost of the meat lovers pizzas with the buy-2-get-1-free special
    meat_lovers_cost = ((9//3) * 2 + (9 % 3)) * (REGULAR_PRICE * (1 - MEAT_DISCOUNT))

    # Calculate the total cost of all the pizzas
    total_cost = triple_cheese_cost + meat_lovers_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())