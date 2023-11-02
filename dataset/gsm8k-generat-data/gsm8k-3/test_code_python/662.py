def solution():
    """Harry has 50 books in his library. His sister Flora has twice as many books and their cousin Gary has half the books Harry has. How many books do the three of them own together?"""
    # Define the number of books Harry has
    harry_books = 50

    # Define the number of books Flora has
    flora_books = harry_books * 2

    # Define the number of books Gary has
    gary_books = harry_books // 2

    # Calculate the total number of books the three of them own
    total_books = harry_books + flora_books + gary_books

    # Display the total number of books
    result = total_books
    return result

print(solution())