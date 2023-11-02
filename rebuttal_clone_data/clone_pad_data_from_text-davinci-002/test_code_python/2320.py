def solution():
    large_pizza = 14
    toppings = 3
    number_of_pizzas = 2
    topping_price = 2
    total_pizza_cost = large_pizza * number_of_pizzas + (toppings * topping_price)
    tip = total_pizza_cost * 0.25
    total_cost = total_pizza_cost + tip
    result = total_cost
    return result

print(solution())