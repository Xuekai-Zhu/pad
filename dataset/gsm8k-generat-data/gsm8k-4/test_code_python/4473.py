def solution():
    """Tony read 23 books, Dean read 12 books and Breanna read 17 books. Tony and Dean read 3 of the same books and all three had read the same book as well. In total how many different books have Tony,
    Dean, and Breanna read?"""
    # Define the number of books read by each person
    tony_books = 23
    dean_books = 12
    breanna_books = 17

    # Define the number of books read by Tony and Dean that are the same
    tony_dean_same = 3

    # Define the number of books read by all three people
    all_same = 1

    # Calculate the total number of books read by all three people
    total_books = tony_books + dean_books + breanna_books - tony_dean_same - all_same

    # return the result
    result = total_books
    return result

print(solution())