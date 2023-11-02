def solution():
    """In the school's library, there are 2300 different books. 80% of all the books are in English, but only 60% of these books were published in the country. How many English-language books have been published outside the country?"""
    # Define the number of books in the library and the percentage of English books
    total_books = 2300
    english_percent = 0.8

    # Calculate the number of English books and the number of English books published in the country
    english_books = total_books * english_percent
    english_country_books = english_books * 0.6

    # Calculate the number of English books published outside the country
    english_foreign_books = english_books - english_country_books

    # Display the number of English books published outside the country
    result = english_foreign_books
    return result

print(solution())