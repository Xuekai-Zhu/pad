def solution():
    """There are 35 books on the cart. There are five fiction books, 4 more non-fiction books than fiction books,
    2 times as many autobiographies as fiction books, and the rest picture books. How many books were picture books?"""
    fiction_books = 5
    non_fiction_books = fiction_books + 4
    autobiography_books = 2 * fiction_books
    total_known_books = fiction_books + non_fiction_books + autobiography_books
    picture_books = 35 - total_known_books
    result = picture_books
    return result

print(solution())