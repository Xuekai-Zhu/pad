def solution():
    # Calculate the total cost of the pizzas
    total_pizza_cost = 5 * 7

    # Calculate the amount of the tip
    tip_amount = total_pizza_cost / 7

    # Calculate the total cost of the order
    total_cost = total_pizza_cost + tip_amount

    # Calculate the change Allen received
    change = 100 - total_cost
    result = change
    return result

print(solution())