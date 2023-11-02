def solution():
    
    pizza_price = 14
    toppings_price = 2
    num_pizzas = 2
    num_toppings = 3
    pizza_cost = (pizza_price + (toppings_price * num_toppings)) * num_pizzas
    tip_percent = 25
    tip_amount = pizza_cost * (tip_percent / 100)
    total_cost = pizza_cost + tip_amount
    result = total_cost
    return result

print(solution())