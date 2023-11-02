def solution():
    total_books = 3000  # Total number of books Susan and Lidia have combined
    lidia_books = total_books * 4 / 5  # Lidia has 4/5 of the total books
    susan_books = total_books - lidia_books  # Susan has the remaining books

    result = susan_books
    return result

print(solution())