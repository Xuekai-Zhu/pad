def solution():
    total_books = 250  # There are 250 books in the library
    tuesday_books = 120  # On Tuesday, 120 books are taken out
    wednesday_books = 35  # On Wednesday, 35 books are returned
    thursday_books = 15  # On Thursday, another 15 books are withdrawn
    remaining_books = total_books - tuesday_books + wednesday_books - thursday_books

    result = remaining_books
    return result

print(solution())