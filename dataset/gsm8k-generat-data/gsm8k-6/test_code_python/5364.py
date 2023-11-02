def solution():
    # Calculate Jenna's total cost
    cost = 3 * 5000  # Jenna pays $3 for each widget
    total_cost = cost + 10000 + 4 * 2500  # cost of widgets, rent, workers' salaries

    # Calculate Jenna's total revenue
    revenue = 8 * 5000  # Jenna sells each widget for $8
    total_revenue = revenue

    # Calculate Jenna's total profit or loss
    profit = total_revenue - total_cost  # total profit before taxes
    tax = 0.2 * profit  # Jenna pays 20% of her total profit in taxes
    total_profit = profit - tax
    result = total_profit
    return result

print(solution())