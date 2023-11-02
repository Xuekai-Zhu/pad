def solution():
    """Last year, the school library purchased 50 new books. This year, it purchased 3 times as many books. If the library had 100 books before it purchased new books last year, how many books are in the library now?"""
    last_year_books = 50
    this_year_books = 3 * last_year_books
    original_books = 100
    total_books = original_books + last_year_books + this_year_books
    result = total_books
    return result

print(solution())