def solution():
    # Calculate the cost of the pizzas without toppings
    cost_pizzas = 2 * 14 * 2  # 2 large pizzas at $14 each

    # Calculate the cost of the toppings
    cost_toppings = 2 * 3 * 2  # 2 pizzas with 3 toppings each at $2 per topping

    # Calculate the total cost of the pizzas and toppings
    total_cost = cost_pizzas + cost_toppings

    # Calculate the 25% tip
    tip = total_cost * 0.25

    # Calculate the final total cost including the tip
    final_cost = total_cost + tip
    result = final_cost
    return result

print(solution())