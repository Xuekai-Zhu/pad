def solution():
    pizza_price = 14  # Price of a large pizza
    topping_price = 2  # Price of each topping
    num_pizzas = 2  # Number of pizzas ordered
    toppings_per_pizza = 3  # Number of toppings per pizza
    tip_percentage = 25  # Percentage of the total cost as tip

    # Calculate the cost of the pizzas before tip
    pizza_cost = pizza_price * num_pizzas
    topping_cost = topping_price * toppings_per_pizza * num_pizzas
    total_cost = pizza_cost + topping_cost

    # Calculate the tip amount
    tip_amount = total_cost * (tip_percentage / 100)

    # Add the tip to the total cost
    total_cost_with_tip = total_cost + tip_amount
    result = total_cost_with_tip
    return result

print(solution())