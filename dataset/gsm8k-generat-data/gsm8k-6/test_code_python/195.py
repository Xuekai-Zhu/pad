def solution():
    # Calculate the total cost of 5 boxes of drinks
    drinks_cost = 5 * 6
    # Calculate the total cost of 10 boxes of pizzas
    pizzas_cost = 10 * 14
    # Calculate the total cost of all items
    total_cost = drinks_cost + pizzas_cost
    # Calculate the change received by Mary
    change = 200 - total_cost
    result = change
    return result

print(solution())