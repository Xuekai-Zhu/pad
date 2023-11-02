def solution():
    """Vincent's bookstore is divided into different kinds of books. His top-selling books are fantasy books. He also sells literature books which cost half of the price of a fantasy book.
    If his fantasy books cost $4 each, and he sold five fantasy books and eight literature books per day, how much money will he earn after five days?"""
    fantasy_price = 4
    literature_price = fantasy_price / 2
    fantasy_books_sold = 5
    literature_books_sold = 8
    total_days = 5
    total_fantasy_earnings = fantasy_price * fantasy_books_sold * total_days
    total_literature_earnings = literature_price * literature_books_sold * total_days
    total_earnings = total_fantasy_earnings + total_literature_earnings
    result = total_earnings
    return result

print(solution())