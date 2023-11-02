def solution():
    # Determine the number of books Lamont has
    lamont_books = 2 * 20

    # Determine the number of books Loris has
    loris_books = lamont_books - 3

    # Determine the total number of books the three have
    total_books = loris_books + lamont_books + 20
    result = total_books
    return result

print(solution())