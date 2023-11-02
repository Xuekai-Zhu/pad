def solution():
    
    thickness = 12
    pages_per_inch = 80
    num_books = 6
    total_pages = thickness * pages_per_inch
    avg_pages_per_book = total_pages / num_books
    result = avg_pages_per_book
    return result

print(solution())