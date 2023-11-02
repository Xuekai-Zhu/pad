def solution():
    """Dianne runs a store that sells books.  37% of her 1000 customers end up returning their books.  Her books all cost 15 dollars apiece.  How much money does she keep in sales after subtracting the returns?"""
    # Define the number of customers and return rate
    NUM_CUSTOMERS = 1000
    RETURN_RATE = 0.37

    # Calculate the number of returning customers
    num_returns = int(NUM_CUSTOMERS * RETURN_RATE)

    # Calculate the total sales revenue
    total_sales = NUM_CUSTOMERS * 15

    # Calculate the total amount of returned books
    return_amount = num_returns * 15

    # Calculate the final revenue after subtracting returns
    final_sales = total_sales - return_amount

    # Display the final revenue
    result = final_sales
    return result

print(solution())