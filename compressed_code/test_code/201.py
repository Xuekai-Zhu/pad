def solution():
    
    total_books = 14
    pages_per_book = 200
    books_read_first_month = 4
    books_remaining = total_books - books_read_first_month
    books_read_second_month = books_remaining / 2
    total_pages = (books_remaining - books_read_second_month) * pages_per_book
    result = total_pages
    return result

print(solution())