def solution():
    # Calculate the price increase of one bottle of wine
    price_increase = 20 * 0.25  # 25% increase on $20.00

    # Calculate the new price of one bottle of wine
    new_price = 20 + price_increase

    # Calculate the total cost of 5 bottles of wine at the new price
    total_cost = new_price * 5

    # Calculate the difference in cost between the original price and new price of 5 bottles of wine
    increase_in_cost = total_cost - (20 * 5)

    result = increase_in_cost
    return result

print(solution())