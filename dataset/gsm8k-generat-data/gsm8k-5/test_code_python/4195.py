def solution():
    books_june = 8  # Katy read 8 books in June
    books_july = 2 * books_june  # Katy read twice as many books in July as she did in June
    books_august = books_july - 3  # Katy read three fewer books in August than she did in July

    # Calculate the total number of books Katy read during the summer
    total_books = books_june + books_july + books_august
    result = total_books
    return result

print(solution())