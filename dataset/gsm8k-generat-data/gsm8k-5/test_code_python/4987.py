def solution():
    current_price = 20.00  # The current price of a bottle of wine is $20.00
    tariff_rate = 0.25  # The new tariffs will increase the price of wine by 25%
    num_bottles = 5  # We want to know how much more expensive 5 bottles of wine will be

    # Calculate the price of a bottle of wine in 2 months after tariffs are imposed
    new_price = current_price * (1 + tariff_rate)

    # Calculate the increase in cost for 5 bottles of wine
    increase_cost = num_bottles * (new_price - current_price)

    result = increase_cost
    return result

print(solution())