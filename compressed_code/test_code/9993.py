def solution():
    
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