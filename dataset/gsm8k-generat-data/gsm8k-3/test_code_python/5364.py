def solution():
    """Jenna runs a wholesale business. She pays $3 for each widget and resells it for $8. Every month she has to pay $10,000 in rent, 20% of her total profit in taxes, and $2,500 each to four workers. If Jenna sells 5000 widgets one month, how much is her total profit or loss?"""
    # Define the cost and selling price of each widget
    COST_PER_WIDGET = 3
    SELLING_PRICE_PER_WIDGET = 8

    # Define the number of widgets sold in one month
    widgets_sold = 5000

    # Calculate the total revenue from selling widgets
    revenue = widgets_sold * SELLING_PRICE_PER_WIDGET

    # Calculate the total cost of purchasing the widgets
    cost = widgets_sold * COST_PER_WIDGET

    # Calculate the total cost of paying workers
    worker_cost = 4 * 2500

    # Calculate the total expenses
    expenses = cost + worker_cost + 10000

    # Calculate the total profit before taxes
    profit_before_taxes = revenue - expenses

    # Calculate the amount of taxes to be paid
    tax = 0.2 * profit_before_taxes

    # Calculate the total profit after taxes
    total_profit = profit_before_taxes - tax

    # Display the total profit or loss
    result = total_profit
    return result

print(solution())