def solution():
    """Dianne runs a store that sells books. 37% of her 1000 customers end up returning their books. Her books all cost 15 dollars apiece. How much money does she keep in sales after subtracting the returns?"""
    # Define the total number of customers and the percentage of returns
    total_customers = 1000
    returns_percentage = 0.37

    # Calculate the number of customers who did not return their books
    non_returns = total_customers * (1 - returns_percentage)

    # Calculate the total sales from books sold
    total_sales = non_returns * 15

    # Return the result
    result = total_sales
    return result

print(solution())