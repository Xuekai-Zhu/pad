def solution():
    """Betty has 20 books, and her sister has 1/4 times more books than Betty. What's the total number of books the two have?"""
    betty_books = 20
    sister_books = betty_books + (betty_books * 1/4)
    total_books = betty_books + sister_books
    result = total_books
    return result

print(solution())