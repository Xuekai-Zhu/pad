def solution():
    """Tony read 23 books, Dean read 12 books and Breanna read 17 books. Tony and Dean read 3 of the same books and all three had read the same book as well. In total how many different books have Tony, Dean, and Breanna read?"""
    tony_books = 23
    dean_books = 12
    breanna_books = 17
    shared_books = 3
    all_three_books = 1
    different_books = tony_books + dean_books + breanna_books - (2 * shared_books) - all_three_books
    result = different_books
    return result

print(solution())