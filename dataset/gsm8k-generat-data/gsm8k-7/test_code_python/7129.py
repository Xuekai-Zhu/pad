def solution():
    initial_books = 5
    unhelpful_books = 3
    new_books = 5
    books_returned = 2
    current_books = 7

    # Calculate the current number of books checked out
    current_books = initial_books - unhelpful_books + new_books - books_returned + current_books
    result = current_books
    return result

print(solution())