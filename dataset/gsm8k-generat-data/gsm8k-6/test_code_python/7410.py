def solution():
    # Calculate the number of books Boris donates to the library
    boris_donate = 24 / 4  # a fourth of 24 books

    # Calculate the number of books Cameron donates to the library
    cameron_donate = 30 / 3  # a third of 30 books

    # Calculate the total number of books left with Boris and Cameron
    total_books = 24 + 30 - boris_donate - cameron_donate

    result = total_books
    return result

print(solution())