def solution():
    # Define the cost of a large pizza and the number of toppings per pizza
    pizza_cost = 14
    toppings_per_pizza = 3

    # Calculate the cost of the toppings for both pizzas
    topping_cost = 2 * toppings_per_pizza * 2  # 2 pizzas

    # Calculate the total cost of the pizzas and toppings
    total_cost = (pizza_cost * 2) + topping_cost

    # Add a 25% tip to the total cost
    total_cost_with_tip = total_cost * 1.25
    result = total_cost_with_tip
    return result

print(solution())