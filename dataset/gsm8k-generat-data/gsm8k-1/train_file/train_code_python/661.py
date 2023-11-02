def solution():
    """Harry has 50 books in his library. His sister Flora has twice as many books and their cousin Gary has half the books Harry has. How many books do the three of them own together?"""
    harry_books = 50
    flora_books = harry_books * 2
    gary_books = harry_books / 2
    total_books = harry_books + flora_books + gary_books
    result = total_books
    return result

print(solution())