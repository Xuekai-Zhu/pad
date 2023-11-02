def solution():
    
    current_sales = 4000 * 12
    target_sales = 60000
    additional_sales = target_sales - current_sales
    additional_sales_per_month = additional_sales / 12
    result = additional_sales_per_month
    return result

print(solution())