def solution():
    
    initial_books = 250
    books_taken_tuesday = 120
    books_returned_wednesday = 35
    books_taken_thursday = 15
    total_books = initial_books - books_taken_tuesday + books_returned_wednesday - books_taken_thursday
    result = total_books
    return result

print(solution())