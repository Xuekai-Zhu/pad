def solution():
     pints_sold = 54
     total_revenue = 216
     sales_revenue = total_revenue / 2
     cost_per_pint = sales_revenue / pints_sold
     result = cost_per_pint * 2
     return result

print(solution())