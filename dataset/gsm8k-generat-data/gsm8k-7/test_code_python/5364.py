def solution():
    cost_per_widget = 3
    selling_price_per_widget = 8
    num_widgets_sold = 5000
    rent = 10000
    tax_rate = 0.2
    num_workers = 4
    wage_per_worker = 2500

    # Calculate the total revenue from selling widgets
    total_revenue = selling_price_per_widget * num_widgets_sold

    # Calculate the total cost of purchasing widgets
    total_cost = cost_per_widget * num_widgets_sold

    # Calculate the total cost of paying wages to workers
    total_wages = num_workers * wage_per_worker

    # Calculate the total profit before taxes
    profit_before_taxes = total_revenue - total_cost - total_wages - rent

    # Calculate the total amount of taxes to be paid
    taxes = profit_before_taxes * tax_rate

    # Calculate the net profit
    net_profit = profit_before_taxes - taxes

    result = net_profit
    return result

print(solution())