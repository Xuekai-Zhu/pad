def solution():
    """Tina is getting $20 for each book she sells. If she realizes a $120 profit on her sales, how many people have she sold the books to if each book costs $5 to make and every customer buys 2 at a time?"""
    book_profit = 20 - 5*2  # profit per pair of books sold
    total_profit = 120
    customers = total_profit / book_profit
    pairs_of_books_sold = customers * 2
    result = pairs_of_books_sold
    return result

print(solution())