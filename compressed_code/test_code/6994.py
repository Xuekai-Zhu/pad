def solution():
    
    books_last_month = 5
    books_this_month = books_last_month * 2
    pages_per_book = 10
    total_pages = (books_last_month + books_this_month) * pages_per_book
    result = total_pages
    return result

print(solution())