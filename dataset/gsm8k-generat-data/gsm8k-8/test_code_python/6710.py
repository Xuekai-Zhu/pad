def solution():
    # Define the cost and revenue per necklace
    charm_cost = 10 * 15
    necklace_price = 200

    # Calculate the profit per necklace
    profit = necklace_price - charm_cost

    # Calculate the total profit for selling 30 necklaces
    total_profit = profit * 30

    result = total_profit
    return result

print(solution())