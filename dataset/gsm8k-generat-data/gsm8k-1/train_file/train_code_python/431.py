def solution():
    """Tina is getting $20 for each book she sells. If she realizes a $120 profit on her sales, how many people have she sold the books to if each book costs $5 to make and every customer buys 2 at a time?"""
    book_profit = 20
    total_profit = 120
    cost_to_make = 5
    books_sold = total_profit / (book_profit - cost_to_make)
    customers = books_sold / 2
    result = customers
    return result

print(solution())