def solution():
    # Define the original prices
    orange_price = 40
    mango_price = 50

    # Increase each price by 15%
    orange_price_increase = orange_price * 0.15
    mango_price_increase = mango_price * 0.15

    new_orange_price = orange_price + orange_price_increase
    new_mango_price = mango_price + mango_price_increase

    # Calculate the total cost of 10 oranges and 10 mangoes at the new prices
    total_cost = (new_orange_price * 10) + (new_mango_price * 10)
    result = total_cost
    return result

print(solution())