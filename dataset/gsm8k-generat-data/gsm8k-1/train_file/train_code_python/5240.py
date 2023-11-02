def solution():
    """Chloe bought chocolate-dipped strawberries at $50 a dozen. She then sold them for $30 for half a dozen during the Mother's Day celebration. How much is Chloe's profit if she sold 50 dozens?"""
    cost_price = 50  # cost for a dozen
    selling_price = 30  # selling price for half a dozen
    strawberries_per_dozen = 12
    strawberries_per_half_dozen = 6
    dozens_sold = 50

    total_cost = cost_price * dozens_sold
    total_revenue = selling_price * 2 * dozens_sold

    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())