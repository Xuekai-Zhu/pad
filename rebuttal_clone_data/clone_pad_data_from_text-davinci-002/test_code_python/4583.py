def solution():
    pizza_price = 10.00
    topping_price = 1.00
    tip_amount = 5.00
    number_of_pizzas = 3
    number_of_toppings = 5
    total_cost = (pizza_price * number_of_pizzas) + (topping_price * number_of_toppings) + tip_amount
    result = total_cost
    return result

print(solution())