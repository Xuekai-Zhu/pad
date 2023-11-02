def solution():
    """Jenna runs a wholesale business. She pays $3 for each widget and resells it for $8. Every month she has to pay $10,000 in rent, 20% of her total profit in taxes, and $2,500 each to four workers. If Jenna sells 5000 widgets one month, how much is her total profit or loss?"""
    widgets_sold = 5000
    widget_cost = 3
    widget_price = 8
    rent = 10000
    workers = 4 * 2500
    revenue = widgets_sold * widget_price
    expenses = widgets_sold * widget_cost + rent + workers
    profit = revenue - expenses
    tax = 0.2 * profit
    total_profit = profit - tax
    result = total_profit
    return result

print(solution())