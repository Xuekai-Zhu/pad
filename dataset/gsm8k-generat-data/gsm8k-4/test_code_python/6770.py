def solution():
    """Five years ago, there were 500 old books in the library. Two years ago, the librarian bought 300 books. Last year, the librarian bought 100 more books than she had bought the previous year. This year, the librarian donated 200 of the library's old books. How many books are in the library now?"""
    # Define the initial number of books
    initial_books = 500

    # Calculate the current number of books after buying new books and donations
    current_books = initial_books + 300 + (300 + 100) - 200

    # return the result
    result = current_books
    return result

print(solution())