def solution():
    # Boris donates a fourth of his books to the library
    boris_donates = 24 / 4
    boris_remaining = 24 - boris_donates

    # Cameron donates a third of his books to the library
    cameron_donates = 30 / 3
    cameron_remaining = 30 - cameron_donates

    # Calculate the total number of books remaining
    total_books = boris_remaining + cameron_remaining
    result = total_books
    return result

print(solution())