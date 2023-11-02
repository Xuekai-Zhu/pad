def solution():
    # Calculate total revenue from tire repairs
    tire_revenue = 300 * 20  # Jim does 300 tire repairs at $20 each
    tire_cost = 300 * 5  # Jim spends $5 on parts for each tire repair
    tire_profit = tire_revenue - tire_cost  # Calculate profit from tire repairs

    # Calculate profit from complex repairs
    complex_revenue = 2 * 300  # Jim does 2 complex repairs for $300 each
    complex_cost = 2 * 50  # Jim spends $50 on parts for each complex repair
    complex_profit = complex_revenue - complex_cost  # Calculate profit from complex repairs

    # Calculate total profit from retail shop
    retail_profit = 2000

    # Calculate total revenue and expenses
    total_revenue = tire_revenue + complex_revenue + retail_profit
    total_expenses = tire_cost + complex_cost + 4000

    # Calculate total profit
    total_profit = total_revenue - total_expenses

    result = total_profit
    return result

print(solution())