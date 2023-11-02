def solution():
    """Tony read 23 books, Dean read 12 books and Breanna read 17 books. Tony and Dean read 3 of the same books and all three had read the same book as well. In total how many different books have Tony, Dean, and Breanna read?"""
    # Define the number of books read by each person
    tony_books = 23
    dean_books = 12
    breanna_books = 17

    # Define the number of books read by Tony and Dean in common
    common_books = 3

    # Calculate the number of books read by Tony and Breanna in common
    tb_common_books = common_books

    # Calculate the number of books read by Dean and Breanna in common
    db_common_books = common_books

    # Calculate the total number of books read by all three
    all_books = tb_common_books + db_common_books + common_books

    # Calculate the number of unique books read by Tony, Dean, and Breanna
    unique_books = tony_books + dean_books + breanna_books - all_books

    # Display the number of unique books
    result = unique_books
    return result

print(solution())