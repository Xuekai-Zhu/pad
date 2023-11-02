def solution():
     cost_per_widget = 3
     selling_price_per_widget = 8
     widgets_sold = 5000
     total_revenue = selling_price_per_widget * widgets_sold
     total_expenses = (cost_per_widget * widgets_sold) + 10000 + ((total_revenue - cost_per_widget * widgets_sold) * 0.2) + (2500 * 4)
     profit_loss = total_revenue - total_expenses
     
     return profit_loss

print(solution())