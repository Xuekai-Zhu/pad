def solution():
    """Chloe bought chocolate-dipped strawberries at $50 a dozen. She then sold them for $30 for half a dozen during the Mother's Day celebration. How much is Chloe's profit if she sold 50 dozens?"""
    # Define the cost of buying a dozen chocolate-dipped strawberries and the selling price for half a dozen
    COST_PER_DOZEN = 50
    SELLING_PRICE_PER_HALF_DOZEN = 30

    # Calculate the cost of buying one chocolate-dipped strawberry
    cost_per_strawberry = COST_PER_DOZEN / 12

    # Calculate the profit per half dozen sold
    profit_per_half_dozen = (SELLING_PRICE_PER_HALF_DOZEN - COST_PER_DOZEN / 2) / 2

    # Calculate the total profit from selling 50 dozens
    total_profit = profit_per_half_dozen * 50 * 2

    # Return the result
    result = total_profit
    return result

print(solution())