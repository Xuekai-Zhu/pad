def solution():
    """Joe's pizzeria has an amazing promotion. If you buy any regular large pizza you can get the next 3 medium pizzas for $5 each. What are your total savings if the regular medium pizza price is $18 and you take full advantage of the promotion?"""
    regular_large_pizza_price = 0 
    regular_medium_pizza_price = 18
    promotion_price = 5
    number_of_medium_pizzas = 3
    total_pizzas = 4 # 1 large pizza + 3 medium pizzas
    savings_per_medium_pizza = regular_medium_pizza_price - promotion_price
    total_savings = number_of_medium_pizzas * savings_per_medium_pizza
    result = total_savings
    return result

print(solution())