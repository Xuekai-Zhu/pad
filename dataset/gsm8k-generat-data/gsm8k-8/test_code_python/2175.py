def solution():
    # Define the number of books Beatrix has
    beatrix_books = 30

    # Calculate the number of books Alannah has
    alannah_books = beatrix_books + 20

    # Calculate the number of books Queen has
    queen_books = alannah_books + (1/5 * alannah_books)

    # Calculate the total number of books
    total_books = beatrix_books + alannah_books + queen_books
    result = total_books
    return result

print(solution())