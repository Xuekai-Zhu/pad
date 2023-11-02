def solution():
    wallet_cost = 22  # Carly wants to buy a wallet that costs $22
    purse_cost = (4 * wallet_cost) - 3  # Carly wants to buy a purse that costs $3 less than 4 times the cost of the wallet

    # Calculate the combined cost of the wallet and purse
    combined_cost = wallet_cost + purse_cost
    result = combined_cost
    return result

print(solution())