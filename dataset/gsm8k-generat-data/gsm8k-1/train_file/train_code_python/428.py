def solution():
    """In the school's library, there are 2300 different books. 80% of all the books are in English, but only 60% of these books were published in the country. How many English-language books have been published outside the country?"""
    total_books = 2300
    english_books = total_books * 0.8
    in_country_books = english_books * 0.6
    outside_country_books = english_books - in_country_books
    result = outside_country_books
    return result

print(solution())