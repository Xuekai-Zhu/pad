def solution():
    
    book_size = 600
    first_week = book_size / 2
    remaining_pages = book_size - first_week
    second_week = 0.3 * remaining_pages
    pages_left = book_size - first_week - second_week
    result = pages_left / 1  
    return result

print(solution())