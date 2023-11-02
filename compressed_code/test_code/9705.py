def solution():
    
    regular_large_pizza_price = 0 
    regular_medium_pizza_price = 18
    promotion_price = 5
    number_of_medium_pizzas = 3
    total_pizzas = 4 
    savings_per_medium_pizza = regular_medium_pizza_price - promotion_price
    total_savings = number_of_medium_pizzas * savings_per_medium_pizza
    result = total_savings
    return result

print(solution())