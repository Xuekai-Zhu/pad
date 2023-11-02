def solution():
    cost_per_dozen = 50  # Chloe bought chocolate-dipped strawberries at $50 a dozen
    sell_price_per_half_dozen = 30  # Chloe sells them for $30 for half a dozen
    items_per_dozen = 2  # There are 2 half dozens in a dozen
    dozens_sold = 50  # Chloe sold 50 dozens

    # Calculate the total cost of buying 50 dozens of strawberries
    total_cost = cost_per_dozen * dozens_sold

    # Calculate the total revenue from selling 50 dozens of strawberries
    total_revenue = (sell_price_per_half_dozen * items_per_dozen * dozens_sold)

    # Calculate Chloe's profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())