def solution():
    # Calculate the total number of book returns
    total_returns = 0.37 * 1000

    # Calculate the total amount of money from sales before returns
    total_sales_before_returns = 1000 * 15

    # Calculate the amount of money from sales after subtracting returns
    total_sales_after_returns = total_sales_before_returns - (total_returns * 15)

    result = total_sales_after_returns
    return result

print(solution())