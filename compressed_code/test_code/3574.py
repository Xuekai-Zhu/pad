def solution():
    
    book_pages = 400
    finished_percent = 0.2
    finished_pages = finished_percent * book_pages
    remaining_pages = book_pages - finished_pages
    result = remaining_pages
    return result

print(solution())