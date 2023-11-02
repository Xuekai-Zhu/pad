def solution():
    
    total_books = 2300
    english_books = 0.8 * total_books
    published_in_country = 0.6 * english_books
    published_outside_country = english_books - published_in_country
    result = published_outside_country
    return result

print(solution())