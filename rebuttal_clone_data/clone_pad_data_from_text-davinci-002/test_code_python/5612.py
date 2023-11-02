def solution():
    books_borrowed = 15
    movies_borrowed = 6
    books_returned = 8
    movies_returned = movies_borrowed / 3
    books_checked_out = 9
    books_remaining = books_borrowed - books_returned + books_checked_out
    movies_remaining = movies_borrowed - movies_returned
    result = [books_remaining, movies_remaining]
    
    return result

print(solution())