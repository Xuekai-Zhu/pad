def solution():
    harry_books = 50  # Harry has 50 books in his library
    flora_books = 2 * harry_books  # Flora has twice as many books as Harry
    gary_books = harry_books / 2  # Gary has half the books Harry has

    # Calculate the total number of books the three of them own together
    total_books = harry_books + flora_books + gary_books
    result = total_books
    return result

print(solution())