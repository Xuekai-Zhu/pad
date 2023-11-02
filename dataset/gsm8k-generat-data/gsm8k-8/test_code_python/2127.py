def solution():
    # Calculate the price of the smartphone at Store A after the discount
    storeA_price = 125 - (0.08*125)

    # Calculate the price of the smartphone at Store B after the discount
    storeB_price = 130 - (0.1*130)

    # Calculate the price difference
    price_difference = storeB_price - storeA_price
    result = price_difference
    return result

print(solution())