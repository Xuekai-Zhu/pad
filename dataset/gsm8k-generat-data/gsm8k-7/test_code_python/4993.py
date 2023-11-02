def solution():
    reg_large_pizza_price = 0  # assume it's not relevant to the problem

    med_pizza_price = 18
    num_med_pizzas = 3

    promo_price = 5
    num_promo_pizzas = 3

    # Calculate the total cost of buying a regular large pizza and the promotional medium pizzas
    total_cost = reg_large_pizza_price + (med_pizza_price * num_med_pizzas) + (promo_price * num_promo_pizzas)

    # Calculate the total cost without the promotion
    total_cost_without_promo = reg_large_pizza_price + (med_pizza_price * 4)

    # Calculate the total savings
    total_savings = total_cost_without_promo - total_cost
    result = total_savings
    return result

print(solution())