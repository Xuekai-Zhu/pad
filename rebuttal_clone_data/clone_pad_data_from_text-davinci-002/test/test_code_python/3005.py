def solution():
    total_customers = 1000
    return_rate = 37
    book_price = 15
    customers_returning = total_customers * (return_rate / 100)
    books_sold = total_customers - customers_returning
    total_sales = books_sold * book_price
    result = total_sales
    return result

print(solution())