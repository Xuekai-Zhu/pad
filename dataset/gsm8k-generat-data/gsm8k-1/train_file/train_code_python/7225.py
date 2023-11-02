def solution():
    """Carly is thinking about buying a wallet that costs $22 and a purse that costs $3 less than four times the cost of the wallet. What is the combined cost of both items?"""
    wallet_cost = 22
    purse_cost = 4 * wallet_cost - 3
    combined_cost = wallet_cost + purse_cost
    result = combined_cost
    return result

print(solution())