def solution():
    
    num_books = 10
    lost_books = 2
    pages_per_book = 100
    remaining_books = num_books - lost_books
    total_pages = remaining_books * pages_per_book
    result = total_pages
    return result

print(solution())