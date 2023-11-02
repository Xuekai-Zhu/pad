def solution():
    """Chloe bought chocolate-dipped strawberries at $50 a dozen. She then sold them for $30 for half a dozen during the Mother's Day celebration. How much is Chloe's profit if she sold 50 dozens?"""
    # Define the cost and selling price of each half dozen of strawberries
    COST_PER_HALF_DOZEN = 25
    PRICE_PER_HALF_DOZEN = 30

    # Define the number of half dozens sold
    half_dozens_sold = 50 * 2

    # Calculate the total cost of the strawberries
    total_cost = half_dozens_sold * COST_PER_HALF_DOZEN

    # Calculate the total revenue from selling the strawberries
    total_revenue = half_dozens_sold * PRICE_PER_HALF_DOZEN

    # Calculate Chloe's profit
    profit = total_revenue - total_cost

    # Display Chloe's profit
    result = profit
    return result

print(solution())