def solution():
    """Harry is ordering pizza. A large pizza is 14. It costs $2 per topping. He orders 2 large pizzas, each with 3 toppings. He then adds a 25% tip. What is the total cost?"""
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