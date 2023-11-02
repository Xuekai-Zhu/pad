def solution():
    """Monica read 16 books last year. This year, she read twice the number of books she read last year. Next year, she wants to read 5 more than twice the number of books she read this year. How many books will Monica read next year?"""
    last_year_books = 16
    this_year_books = 2 * last_year_books
    next_year_books = 2 * this_year_books + 5
    result = next_year_books
    return result

print(solution())