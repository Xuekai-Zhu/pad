def solution():
    # Calculate the new price of lemons
    lemon_price_increase = 4  # The price of lemons has risen by $4
    new_lemon_price = 8 + lemon_price_increase  # The new price of lemons is $8 + $4 = $12

    # Calculate the new price of grapes
    grape_price_increase = lemon_price_increase / 2  # The price of grapes has increased by half of the increase in the price of lemons
    new_grape_price = 7 + grape_price_increase  # The new price of grapes is $7 + $2 = $9

    # Calculate the total amount collected from selling the fruits
    total_amount_lemons = 80 * new_lemon_price  # Erick sold 80 lemons at the new price
    total_amount_grapes = 140 * new_grape_price  # Erick sold 140 grapes at the new price
    total_amount = total_amount_lemons + total_amount_grapes

    result = total_amount
    return result

print(solution())