def solution():
    """Alannah, Beatrix, and Queen are preparing for the new school year and have been given books by their parents. Alannah has 20 more books than Beatrix. Queen has 1/5 times more books than Alannah. If Beatrix has 30 books, how many books do the three have together?"""
    beatrix_books = 30
    alannah_books = beatrix_books + 20
    queen_books = alannah_books * 1.2
    total_books = beatrix_books + alannah_books + queen_books
    result = total_books
    return result

print(solution())