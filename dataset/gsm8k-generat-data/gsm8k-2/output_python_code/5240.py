def solution():
    """Chloe bought chocolate-dipped strawberries at $50 a dozen. She then sold them for $30 for half a dozen during the Mother's Day celebration. How much is Chloe's profit if she sold 50 dozens?"""
    cost_per_dozen = 50
    selling_price_per_half_dozen = 30
    strawberries_per_dozen = 12
    strawberries_per_half_dozen = 6
    dozens_sold = 50

    cost_per_strawberry = cost_per_dozen / strawberries_per_dozen  # Cost per strawberry
    revenue_per_half_dozen = selling_price_per_half_dozen  # Revenue per half dozen
    cost_per_half_dozen = cost_per_strawberry * strawberries_per_half_dozen  # Cost per half dozen
    profit_per_half_dozen = revenue_per_half_dozen - cost_per_half_dozen  # Profit per half dozen
    profit_per_dozen = 2 * profit_per_half_dozen  # Profit per dozen
    total_profit = profit_per_dozen * dozens_sold  # Total profit

    result = total_profit
    return result

print(solution())