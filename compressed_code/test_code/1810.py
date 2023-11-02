def solution():
    
    pizza_cost = 14
    toppings_cost = 2
    num_pizzas = 2
    num_toppings = 3
    subtotal = (pizza_cost * num_pizzas) + (toppings_cost * num_toppings * num_pizzas)
    tip_percent = 0.25
    tip_amount = subtotal * tip_percent
    total_cost = subtotal + tip_amount
    result = total_cost
    return result

print(solution())