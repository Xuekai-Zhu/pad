def solution():
    """Harry is ordering pizza. A large pizza is 14. It costs $2 per topping. He orders 2 large pizzas, each with 3 toppings. He then adds a 25% tip. What is the total cost?"""
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