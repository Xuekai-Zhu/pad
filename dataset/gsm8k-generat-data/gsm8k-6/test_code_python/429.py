def solution():
    total_books = 2300  # total number of books in the library
    english_books = 0.8 * total_books  # number of English-language books
    english_books_local = 0.6 * english_books  # number of English-language books published in the country
    english_books_foreign = english_books - english_books_local  # number of English-language books published outside the country
    result = english_books_foreign
    return result

print(solution())