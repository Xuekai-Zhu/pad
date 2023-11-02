def solution():
    """There are 50 books in a small library. Half of them are written in English, and 10% in German. All others are written in Spanish. How many Spanish books are there?"""
    total_books = 50
    english_books = total_books / 2
    german_books = total_books * 0.1
    spanish_books = total_books - english_books - german_books
    result = spanish_books
    return result

print(solution())