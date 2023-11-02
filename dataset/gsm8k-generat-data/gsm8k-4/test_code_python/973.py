def solution():
    """The buyers who came to Mr. Brandon's shop yesterday bought goods worth $80. If 2/5 of the total amount of sales Mr. Brandon made yesterday were credit sales, and the rest were cash sales, how much did Mr. Brandon get from cash sales?"""
    # Define the total amount of sales and the percentage of credit sales
    total_sales = 80
    credit_sales_percentage = 0.4

    # Calculate the amount of credit sales
    credit_sales = total_sales * credit_sales_percentage

    # Calculate the amount of cash sales
    cash_sales = total_sales - credit_sales

    # return the result
    result = cash_sales
    return result

print(solution())