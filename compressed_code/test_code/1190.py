def solution():
    
    last_month_books = 5
    this_month_books = last_month_books * 2
    book_pages = 10
    total_pages = (last_month_books + this_month_books) * book_pages
    result = total_pages
    return result

print(solution())