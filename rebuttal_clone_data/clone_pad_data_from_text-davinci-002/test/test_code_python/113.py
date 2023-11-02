def solution():
    
    stack_thickness = 12
    pages_per_inch = 80
    total_pages = stack_thickness * pages_per_inch
    num_books = 6
    pages_per_book = total_pages / num_books
    result = pages_per_book
    return result

print(solution())