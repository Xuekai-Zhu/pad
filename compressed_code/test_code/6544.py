def solution():
    
    total_sales = 80
    credit_sales_percent = 2/5
    credit_sales = total_sales * credit_sales_percent
    cash_sales = total_sales - credit_sales
    result = cash_sales
    return result

print(solution())