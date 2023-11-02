def solution():
    """Jenna runs a wholesale business. She pays $3 for each widget and resells it for $8. Every month she has to pay $10,000 in rent, 20% of her total profit in taxes, and $2,500 each to four workers. If Jenna sells 5000 widgets one month, how much is her total profit or loss?"""
    widget_cost = 3
    widget_price = 8
    rent = 10000
    worker_payment = 4 * 2500
    widgets_sold = 5000
    revenue = widgets_sold * widget_price
    cost = widgets_sold * widget_cost
    profit = revenue - cost - rent - worker_payment
    profit_after_tax = profit * 0.8
    result = profit_after_tax
    return result

print(solution())