def solution():
    """Last year, the school library purchased 50 new books. This year, it purchased 3 times as many books. If the library had 100 books before it purchased new books last year, how many books are in the library now?"""
    # Define the initial number of books in the library
    initial_books = 100

    # Calculate the total number of books purchased
    total_purchased = 50 + 3*50

    # Calculate the current total number of books in the library
    current_books = initial_books + total_purchased

    # return the result
    result = current_books
    return result

print(solution())