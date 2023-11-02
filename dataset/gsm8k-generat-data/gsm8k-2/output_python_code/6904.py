def solution():
    """Peter has 20 books. He has read 40% of them. His brother has read 10% of them. How many more of these books has Peter read than his brother?"""
    total_books = 20
    peter_books_read = total_books * 0.4
    brother_books_read = total_books * 0.1
    books_more_read = peter_books_read - brother_books_read
    result = books_more_read
    return result

print(solution())