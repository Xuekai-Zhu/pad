def solution():
    
    total_books = 2300
    english_books = total_books * 0.8
    in_country_books = english_books * 0.6
    outside_country_books = english_books - in_country_books
    result = outside_country_books
    return result

print(solution())