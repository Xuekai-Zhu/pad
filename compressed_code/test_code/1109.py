def solution():
    
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