def solution():
    widgets_sold = 5000  # Jenna sells 5000 widgets
    widget_cost = 3  # Jenna pays $3 for each widget
    widget_price = 8  # Jenna sells each widget for $8

    # Calculate the total revenue from selling widgets
    total_revenue = widgets_sold * widget_price

    # Calculate the total cost of goods sold
    cogs = widgets_sold * widget_cost

    # Calculate the total cost of other expenses
    rent = 10000  # Jenna pays $10,000 in rent every month
    pay_worker = 2500 * 4  # Jenna pays $2,500 each to four workers
    other_expenses = rent + pay_worker

    # Calculate the total profit before taxes
    total_profit = total_revenue - cogs - other_expenses

    # Calculate the total taxes due
    taxes = 0.2 * total_profit

    # Calculate the final profit after taxes
    final_profit = total_profit - taxes
    result = final_profit
    return result

print(solution())