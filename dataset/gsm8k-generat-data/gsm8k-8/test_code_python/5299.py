def solution():
    # Define the number of customers and the return percentage
    num_customers = 1000
    return_percent = 0.37

    # Calculate the number of returns and the number of sales
    num_returns = num_customers * return_percent
    num_sales = num_customers - num_returns

    # Calculate the total amount of money earned in sales
    total_sales = num_sales * 15

    # Calculate the amount of money kept after subtracting returns
    money_kept = total_sales - (num_returns * 15)

    result = money_kept
    return result

print(solution())