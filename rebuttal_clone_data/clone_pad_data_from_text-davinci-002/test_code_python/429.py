def solution():
    library_books = 2300
    english_books = library_books * 0.8
    books_not_published_in_country = english_books * 0.6
    result = english_books - books_not_published_in_country
    return result

print(solution())