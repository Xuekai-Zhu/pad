def solution():
    """Piazzanos Pizzeria has a buy-1-get-1-free special on triple cheese pizzas, and a buy-2-get-1-free special on meat lovers pizzas. If the standard price for a pizza is $5, how much does it cost, in dollars, to purchase 10 triple cheese and 9 meat lovers pizzas using the special pricing?"""
    triple_cheese_price = 5
    meat_lovers_price = 5
    total_price = 0
    triple_cheese_special = 2
    meat_lovers_special = 3
    num_triple_cheese = 10
    num_meat_lovers = 9
    num_triple_cheese_purchases = num_triple_cheese // triple_cheese_special
    num_meat_lovers_purchases = num_meat_lovers // meat_lovers_special
    total_price += num_triple_cheese_purchases * triple_cheese_price
    total_price += (num_triple_cheese - num_triple_cheese_purchases) * triple_cheese_price
    total_price += num_meat_lovers_purchases * 2 * meat_lovers_price
    total_price += (num_meat_lovers - num_meat_lovers_purchases * 2) * meat_lovers_price
    result = total_price
    return result

print(solution())