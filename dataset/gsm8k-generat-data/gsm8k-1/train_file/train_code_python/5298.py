def solution():
    """Dianne runs a store that sells books. 37% of her 1000 customers end up returning their books. Her books all cost 15 dollars apiece. How much money does she keep in sales after subtracting the returns?"""
    num_customers = 1000
    percent_returns = 37
    num_returns = num_customers * (percent_returns / 100)
    num_sales = num_customers - num_returns
    book_cost = 15
    total_sales = num_sales * book_cost
    result = total_sales
    return result

print(solution())