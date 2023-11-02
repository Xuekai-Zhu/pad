def solution():
    """Joe's pizzeria has an amazing promotion. If you buy any regular large pizza you can get the next 3 medium pizzas for $5 each. What are your total savings if the regular medium pizza price is $18 and you take full advantage of the promotion?"""
    regular_large_pizza_price = 0 # unknown since not given in the problem
    regular_medium_pizza_price = 18
    num_medium_pizzas = 3
    promo_medium_pizza_price = 5
    num_sets_of_medium_pizzas = regular_large_pizza_price // 1 # get floor division
    total_regular_medium_pizza_price = num_sets_of_medium_pizzas * 3 * regular_medium_pizza_price
    total_promo_medium_pizza_price = num_sets_of_medium_pizzas * num_medium_pizzas * promo_medium_pizza_price
    total_savings = total_regular_medium_pizza_price - total_promo_medium_pizza_price
    result = total_savings
    return result

print(solution())