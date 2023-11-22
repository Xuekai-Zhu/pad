def solution():
    
    middle_shelf_books = 10
    bottom_shelf_books = middle_shelf_books * 2
    top_shelf_books = bottom_shelf_books - 5
    total_books = 110
    bookcases_needed = (total_books - (middle_shelf_books + bottom_shelf_books + top_shelf_books)) // 2
    result = bookcases_needed
    return result

print(solution())