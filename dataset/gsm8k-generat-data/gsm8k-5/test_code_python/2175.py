def solution():
    beatrix_books = 30  # Beatrix has 30 books
    alannah_books = beatrix_books + 20  # Alannah has 20 more books than Beatrix
    queen_books = alannah_books + (1/5 * alannah_books)  # Queen has 1/5 more books than Alannah

    # Calculate the total number of books the three have together
    total_books = beatrix_books + alannah_books + queen_books
    result = total_books
    return result

print(solution())