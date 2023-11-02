def solution():
    """In the school's library, there are 2300 different books. 80% of all the books are in English, but only 60% of these books were published in the country. How many English-language books have been published outside the country?"""
    # Define the total number of books and the percentage of English-language books
    total_books = 2300
    english_percentage = 0.8

    # Calculate the number of English-language books
    english_books = total_books * english_percentage

    # Calculate the percentage of English-language books published in the country
    country_percentage = 0.6

    # Calculate the number of English-language books published outside the country
    outside_books = english_books * (1 - country_percentage)

    # return the result
    result = outside_books
    return result

print(solution())