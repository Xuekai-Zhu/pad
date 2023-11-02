def solution():
    # Calculate the new prices of the oranges and the mangoes
    new_orange_price = 40 * 1.15  # increase of 15%
    new_mango_price = 50 * 1.15  # increase of 15%

    # Calculate the total cost of buying 10 oranges and 10 mangoes at the new prices
    total_cost = 10 * new_orange_price + 10 * new_mango_price
    result = total_cost
    return result

print(solution())