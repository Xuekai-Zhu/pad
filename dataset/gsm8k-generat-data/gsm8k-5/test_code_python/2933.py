def solution():
    total_books = 235  # There are initially 235 books in the library
    books_taken_out = 227  # On Tuesday, 227 books are taken out
    books_brought_back = 56  # On Thursday, 56 books are brought back
    books_taken_out_again = 35  # On Friday, 35 books are taken out again

    # Calculate the total number of books after all the transactions
    total_books = total_books - books_taken_out + books_brought_back - books_taken_out_again
    result = total_books
    return result

print(solution())