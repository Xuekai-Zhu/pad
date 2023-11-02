def solution():
    """Jenna runs a wholesale business. She pays $3 for each widget and resells it for $8. Every month she has to pay $10,000 in rent, 20% of her total profit in taxes, and $2,500 each to four workers. If Jenna sells 5000 widgets one month, how much is her total profit or loss?"""
    # Define the cost and selling price of each widget
    widget_cost = 3
    widget_price = 8

    # Define the number of widgets sold
    widgets_sold = 5000

    # Calculate the revenue from selling the widgets
    revenue = widget_price * widgets_sold

    # Calculate the cost of buying the widgets
    cost = widget_cost * widgets_sold

    # Calculate the total expenses including rent and worker salaries
    expenses = 10000 + 4 * 2500

    # Calculate the net profit before taxes
    net_profit = revenue - cost - expenses

    # Calculate the amount of taxes to be paid
    taxes = 0.2 * net_profit

    # Calculate the final profit or loss
    final_profit = net_profit - taxes

    # return the result
    result = final_profit
    return result

print(solution())