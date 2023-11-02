def solution():
    
    total_customers = 1000
    return_percent = 0.37
    books_sold = total_customers - (total_customers * return_percent)
    price_per_book = 15
    total_sales = books_sold * price_per_book
    result = total_sales
    return result

print(solution())