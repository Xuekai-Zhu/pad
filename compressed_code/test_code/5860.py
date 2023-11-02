def solution():
    
    pages_per_day = 20
    pages_per_book = 400
    num_books = 3
    total_pages = pages_per_book * num_books
    days_to_write = total_pages // pages_per_day
    result = days_to_write
    return result

print(solution())