def solution():
    
    total_pages = 800
    book1_pages = 500
    book1_read = 0.8 * book1_pages
    book2_pages = 1000
    book2_read = book2_pages * (1/5)
    pages_left = total_pages - (book1_read + book2_read)
    result = pages_left
    return result

print(solution())