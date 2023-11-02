def solution():
    num_customers = 1000
    return_rate = 0.37
    book_price = 15

    # Calculate the number of customers who do not return their books
    num_non_return_customers = num_customers * (1 - return_rate)

    # Calculate the total sales revenue from non-returning customers
    total_sales = num_non_return_customers * book_price

    result = total_sales
    return result

print(solution())