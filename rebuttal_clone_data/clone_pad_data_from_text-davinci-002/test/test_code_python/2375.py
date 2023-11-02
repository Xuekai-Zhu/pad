def solution():
    books_read_june = 8
    books_read_july = 2 * books_read_june
    books_read_august = books_read_july - 3
    total_books_read = books_read_june + books_read_july + books_read_august
    result = total_books_read
    return result

print(solution())