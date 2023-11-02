def solution():
    original_orange_price = 40
    original_mango_price = 50
    price_increase = 0.15  # 15% increase in price

    # Calculate the new prices for 1 orange and 1 mango after the price increase
    new_orange_price = original_orange_price * (1 + price_increase)
    new_mango_price = original_mango_price * (1 + price_increase)

    # Calculate the total cost of buying 10 oranges and 10 mangoes at the new prices
    total_cost = (new_orange_price * 10) + (new_mango_price * 10)
    result = total_cost
    return result

print(solution())