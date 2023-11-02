def solution():
    total_sales = 80
    credit_sales_ratio = 2/5

    # Calculate the amount of credit sales
    credit_sales = total_sales * credit_sales_ratio

    # Calculate the amount of cash sales
    cash_sales = total_sales - credit_sales
    result = cash_sales
    return result

print(solution())