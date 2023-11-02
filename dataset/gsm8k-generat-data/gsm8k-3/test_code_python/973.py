def solution():
    """The buyers who came to Mr. Brandon's shop yesterday bought goods worth $80. If 2/5 of the total amount of sales Mr. Brandon made yesterday were credit sales, and the rest were cash sales, how much did Mr. Brandon get from cash sales?"""
    # Define the total sales for the day and the fraction of sales that were credit sales
    total_sales = 80
    credit_fraction = 2/5

    # Calculate the total amount of credit sales and the total amount of cash sales
    credit_sales = total_sales * credit_fraction
    cash_sales = total_sales - credit_sales

    # Display the amount of cash sales
    result = cash_sales
    return result

print(solution())