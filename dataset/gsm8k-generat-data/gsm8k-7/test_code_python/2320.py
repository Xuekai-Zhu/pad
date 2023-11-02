def solution():
    large_pizza_price = 14
    topping_price = 2
    num_pizzas = 2
    num_toppings_per_pizza = 3
    tip_percentage = 0.25  # 25% tip

    # Calculate the total cost of the pizzas without the tip
    total_pizza_cost = num_pizzas * (large_pizza_price + (num_toppings_per_pizza * topping_price))

    # Calculate the tip amount
    tip_amount = total_pizza_cost * tip_percentage

    # Calculate the total cost with the tip
    total_cost = total_pizza_cost + tip_amount
    result = total_cost
    return result

print(solution())