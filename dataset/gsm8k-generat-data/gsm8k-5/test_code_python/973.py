def solution():
    total_sales = 80  # Buyers bought goods worth $80
    credit_sales = (2 / 5) * total_sales  # 2/5 of total sales were credit sales
    cash_sales = total_sales - credit_sales  # Cash sales make up the remaining sales

    result = cash_sales
    return result

print(solution())