def solution():
    """Boris has 24 books and he donates a fourth of his books to the library.
    Cameron has 30 books and he donates a third of his books to the library.
    After donating their books, how many books in total do Boris and Cameron have together?"""

    # Boris donates a fourth of his books to the library
    boris_books = 24
    boris_donated = boris_books // 4
    boris_left = boris_books - boris_donated
    
    # Cameron donates a third of his books to the library
    cameron_books = 30
    cameron_donated = cameron_books // 3
    cameron_left = cameron_books - cameron_donated
    
    # Total books left after donations
    total_books = boris_left + cameron_left
    
    # Display the total number of books
    result = total_books
    return result

print(solution())