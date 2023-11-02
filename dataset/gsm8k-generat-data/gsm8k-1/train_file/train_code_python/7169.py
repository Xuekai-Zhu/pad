def solution():
    """Monica read 16 books last year. This year, she read twice the number of books she read last year. Next year, she wants to read 5 more than twice the number of books she read this year. How many books will Monica read next year?"""
    books_last_year = 16
    books_this_year = books_last_year * 2
    books_next_year = (books_this_year * 2) + 5
    result = books_next_year
    return result

print(solution())