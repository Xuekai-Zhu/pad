def solution():
    """Boris has 24 books and he donates a fourth of his books to the library. Cameron has 30 books and he donates a third of his books to the library. After donating their books, how many books in total do Boris and Cameron have together?"""
    boris_books = 24
    boris_donated = boris_books / 4
    cameron_books = 30
    cameron_donated = cameron_books / 3
    total_books = boris_books + cameron_books - boris_donated - cameron_donated
    result = total_books
    return result

print(solution())