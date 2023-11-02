def solution():
    total_books = 2300
    english_books = total_books * 0.8
    english_books_published_in_country = english_books * 0.6
    english_books_published_outside_country = english_books - english_books_published_in_country
    result = english_books_published_outside_country
    return result

print(solution())