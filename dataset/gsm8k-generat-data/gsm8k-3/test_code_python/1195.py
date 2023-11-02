def solution():
    """Last year, the school library purchased 50 new books. This year, it purchased 3 times as many books. If the library had 100 books before it purchased new books last year, how many books are in the library now?"""
    # Define the number of books purchased last year and this year
    books_last_year = 50
    books_this_year = 3 * books_last_year

    # Calculate the total number of books in the library now
    total_books = 100 + books_last_year + books_this_year

    # Display the total number of books in the library now
    result = total_books
    return result

print(solution())