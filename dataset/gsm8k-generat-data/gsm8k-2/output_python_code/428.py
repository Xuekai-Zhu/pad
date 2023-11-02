def solution():
    """In the school's library, there are 2300 different books. 80% of all the books are in English, but only 60% of these books were published in the country. How many English-language books have been published outside the country?"""
    total_books = 2300
    english_books = 0.8 * total_books
    published_in_country = 0.6 * english_books
    published_outside_country = english_books - published_in_country
    result = published_outside_country
    return result

print(solution())