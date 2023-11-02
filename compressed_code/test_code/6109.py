def solution():
    
    book_profit = 20
    total_profit = 120
    cost_to_make = 5
    books_sold = total_profit / (book_profit - cost_to_make)
    customers = books_sold / 2
    result = customers
    return result

print(solution())