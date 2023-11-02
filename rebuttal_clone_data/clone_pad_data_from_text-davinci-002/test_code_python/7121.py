def solution():
     cost_per_pan = 10
     number_of_pans = 20
     sales_price = 25
     total_revenue = number_of_pans * sales_price
     total_expenses = cost_per_pan * number_of_pans
     net_profit = total_revenue - total_expenses
     result = net_profit
 
     return result

print(solution())