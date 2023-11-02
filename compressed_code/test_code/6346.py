def solution():
    
    books_per_month = 3
    book_price = 20
    cost_per_year = books_per_month * book_price * 12
    sale_price = 500
    loss = cost_per_year - sale_price
    result = loss
    return result

print(solution())