def solution():
    # Total number of books in the library
    total_books = 2300

    # Number of books in English
    english_books = total_books * 0.8

    # Number of English books published in the country
    english_books_country = english_books * 0.6

    # Number of English books published outside the country
    english_books_outside_country = english_books - english_books_country
    result = english_books_outside_country
    return result

print(solution())