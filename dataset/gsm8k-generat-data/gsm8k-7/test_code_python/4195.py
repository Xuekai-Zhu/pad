def solution():
    books_in_june = 8
    books_in_july = 2 * books_in_june
    books_in_august = books_in_july - 3
    
    total_books = books_in_june + books_in_july + books_in_august
    result = total_books
    return result

print(solution())