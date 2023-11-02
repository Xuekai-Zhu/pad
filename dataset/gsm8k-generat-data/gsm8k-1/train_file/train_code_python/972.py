def solution():
    """The buyers who came to Mr. Brandon's shop yesterday bought goods worth $80. If 2/5 of the total amount of sales Mr. Brandon made yesterday were credit sales, and the rest were cash sales, how much did Mr. Brandon get from cash sales?"""
    total_sales = 80
    credit_sales_percent = 2/5
    credit_sales = total_sales * credit_sales_percent
    cash_sales = total_sales - credit_sales
    result = cash_sales
    return result

print(solution())