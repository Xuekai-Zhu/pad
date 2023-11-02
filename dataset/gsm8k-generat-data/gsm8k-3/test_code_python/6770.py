def solution():
    """Five years ago, there were 500 old books in the library. Two years ago, the librarian bought 300 books. Last year, the librarian bought 100 more books than she had bought the previous year. This year, the librarian donated 200 of the library's old books. How many books are in the library now?"""
    # Define the initial number of old books
    old_books = 500

    # Calculate the number of books added over the past 2 years
    added_books = 300 + (300 + 100)

    # Calculate the current number of books
    current_books = old_books + added_books - 200

    # Display the current number of books
    result = current_books
    return result

print(solution())