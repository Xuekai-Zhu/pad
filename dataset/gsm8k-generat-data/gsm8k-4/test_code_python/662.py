def solution():
    """Harry has 50 books in his library. His sister Flora has twice as many books and their cousin Gary has half the books Harry has. How many books do the three of them own together?"""
    # Define the number of books each person has
    harry_books = 50
    flora_books = 2 * harry_books
    gary_books = harry_books / 2

    # Calculate the total number of books
    total_books = harry_books + flora_books + gary_books

    # return the result
    result = total_books
    return result

print(solution())