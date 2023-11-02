def solution():
    """Boris has 24 books and he donates a fourth of his books to the library. Cameron has 30 books and he donates a third of his books to the library. After donating their books, how many books in total do Boris and Cameron have together?"""
    # Define the initial number of books for Boris and Cameron
    boris_books = 24
    cameron_books = 30

    # Calculate the number of books Boris donates to the library
    boris_donated = boris_books // 4

    # Calculate the number of books Cameron donates to the library
    cameron_donated = cameron_books // 3

    # Calculate the number of books Boris and Cameron have left
    boris_left = boris_books - boris_donated
    cameron_left = cameron_books - cameron_donated

    # Calculate the total number of books they have left together
    total_books = boris_left + cameron_left

    # return the result
    result = total_books
    return result

print(solution())