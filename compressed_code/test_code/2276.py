def solution():
    
    current_sales = 4000 * 12
    target_sales = 60000
    extra_sales_per_month = (target_sales - current_sales) / 12
    result = extra_sales_per_month
    return result

print(solution())