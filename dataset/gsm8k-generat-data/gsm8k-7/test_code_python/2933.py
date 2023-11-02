def solution():
    total_books = 235
    books_taken_tuesday = 227
    books_brought_thursday = 56
    books_taken_friday = 35

    # Calculate the total number of books taken out and brought back
    net_books_taken = books_taken_tuesday - books_brought_thursday + books_taken_friday

    # Subtract the net number of books taken out from the total number of books in the library
    total_books = total_books - net_books_taken
    result = total_books
    return result

print(solution())