def solution():
    """Five years ago, there were 500 old books in the library. Two years ago, the librarian bought 300 books. Last year, the librarian bought 100 more books than she had bought the previous year. This year, the librarian donated 200 of the library's old books. How many books are in the library now?"""
    old_books = 500
    current_books = old_books - 200 + 300 + 400 - 200
    result = current_books
    return result

print(solution())