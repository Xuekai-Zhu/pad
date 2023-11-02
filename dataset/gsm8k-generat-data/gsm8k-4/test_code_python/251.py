def solution():
    """One pie costs $4 for a piece. Each pie is having 3 pieces. During one hour the bakery can make 12 pies. Creating one pie costs the bakery $0.5. Considering the bakery would be able to sell all pie pieces, how much money would it make?"""
    # Define the cost and price of one pie
    PIE_COST = 0.5
    PIE_PRICE = 4

    # Calculate the profit of selling one pie
    PIE_PROFIT = PIE_PRICE - PIE_COST

    # Calculate the total profit of selling 12 pies
    TOTAL_PROFIT = PIE_PROFIT * 3 * 12

    result = TOTAL_PROFIT
    return result

print(solution())