def solution():
    boris_books = 24
    cameron_books = 30

    # Boris donates a fourth of his books to the library
    boris_donated = boris_books / 4
    boris_remaining = boris_books - boris_donated

    # Cameron donates a third of his books to the library
    cameron_donated = cameron_books / 3
    cameron_remaining = cameron_books - cameron_donated

    # Calculate the total number of books Boris and Cameron have remaining
    total_books = boris_remaining + cameron_remaining
    result = total_books
    return result

print(solution())