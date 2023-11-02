def solution():
    """Dianne runs a store that sells books. 37% of her 1000 customers end up returning their books. Her books all cost 15 dollars apiece. How much money does she keep in sales after subtracting the returns?"""
    total_customers = 1000
    return_percent = 0.37
    books_sold = total_customers - (total_customers * return_percent)
    price_per_book = 15
    total_sales = books_sold * price_per_book
    result = total_sales
    return result

print(solution())