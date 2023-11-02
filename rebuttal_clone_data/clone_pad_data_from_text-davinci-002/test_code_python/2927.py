def solution():
     sales_per_month = 4000
     desired_sales_per_year = 60000
     months_per_year = 12
     desired_sales_per_month = desired_sales_per_year / months_per_year
     needed_sales_per_month = desired_sales_per_month - sales_per_month
     result = needed_sales_per_month
     return result

print(solution())