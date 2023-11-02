def solution():
    """Marj has two $20 bills, three $5 bills, and $4.50 in loose coins in her wallet. If she buys a cake that costs $17.50, how much money will be left in her wallet?"""
    # Define the initial amount of money in Marj's wallet
    wallet_total = (2 * 20) + (3 * 5) + 4.5

    # Define the cost of the cake
    cake_cost = 17.5

    # Subtract the cost of the cake from the total amount of money in Marj's wallet
    wallet_total -= cake_cost

    # Return the money left in Marj's wallet
    result = wallet_total
    return result

print(solution())