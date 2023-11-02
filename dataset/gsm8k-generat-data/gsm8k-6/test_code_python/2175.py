def solution():
    # Number of books Beatrix has
    books_Beatrix = 30

    # Number of books Alannah has and Queen has
    books_Alannah = books_Beatrix + 20
    books_Queen = books_Alannah + (1/5)*books_Alannah

    # Total number of books the three have together
    total_books = books_Beatrix + books_Alannah + books_Queen
    result = total_books
    return result

print(solution())