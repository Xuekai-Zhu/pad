def solution():
    """Gemma ordered four pizzas at $10 each, and she gave a $5 tip to the delivery person. How much change did she get back if she gives one fifty-dollar bill?"""
    pizza_cost = 10
    num_pizzas = 4
    total_cost = pizza_cost * num_pizzas
    tip = 5
    total_cost += tip
    amount_paid = 50
    change = amount_paid - total_cost
    result = change
    return result

print(solution())