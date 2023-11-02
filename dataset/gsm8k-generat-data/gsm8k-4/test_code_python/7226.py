def solution():
    """Carly is thinking about buying a wallet that costs $22 and a purse that costs $3 less than four times the cost of the wallet. What is the combined cost of both items?"""
    # Define the cost of the wallet
    wallet_cost = 22

    # Calculate the cost of the purse
    purse_cost = 4 * wallet_cost - 3

    # Calculate the total cost of both items
    total_cost = wallet_cost + purse_cost

    # return the result
    result = total_cost
    return result

print(solution())