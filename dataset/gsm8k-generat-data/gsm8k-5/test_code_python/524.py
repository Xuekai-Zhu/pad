def solution():
    total_books = 336  # There are 336 books in the library
    books_taken_out = 124  # On Monday, 124 books are taken out
    books_brought_back = 22  # On Tuesday, 22 books are brought back

    # Calculate the total number of books after Monday and Tuesday
    total_books_after = total_books - books_taken_out + books_brought_back
    result = total_books_after
    return result

print(solution())