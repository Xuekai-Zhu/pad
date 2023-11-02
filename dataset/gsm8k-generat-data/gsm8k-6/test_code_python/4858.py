def solution():
    # Calculate the new price of lemons
    new_lemon_price = 8 + 4  # the price of lemons has risen by $4 for each lemon

    # Calculate the increase in price for grapes
    grape_price_increase = 4 / 2  # the price of grapes has increased by half the price that the price of lemon increased by

    # Calculate the new price of grapes
    new_grape_price = 7 + grape_price_increase

    # Calculate the total amount of money from selling the fruits
    total_money = (80 * new_lemon_price) + (140 * new_grape_price)
    result = total_money
    return result

print(solution())