def solution():
    
    initial_books = 336
    monday_books_out = 124
    tuesday_books_in = 22
    remaining_books = initial_books - monday_books_out + tuesday_books_in
    result = remaining_books
    return result

print(solution())