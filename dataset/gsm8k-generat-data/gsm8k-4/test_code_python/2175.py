def solution():
    """Alannah, Beatrix, and Queen are preparing for the new school year and have been given books by their parents. Alannah has 20 more books than Beatrix. Queen has 1/5 times more books than Alannah. If Beatrix has 30 books, how many books do the three have together?"""
    # Define the number of books that Beatrix has
    beatrix_books = 30

    # Calculate the number of books that Alannah has
    alannah_books = beatrix_books + 20

    # Calculate the number of books that Queen has
    queen_books = alannah_books * 1.2

    # Calculate the total number of books
    total_books = beatrix_books + alannah_books + queen_books

    # return the result
    result = int(total_books)
    return result

print(solution())