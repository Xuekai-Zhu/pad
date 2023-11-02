def solution():
    
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