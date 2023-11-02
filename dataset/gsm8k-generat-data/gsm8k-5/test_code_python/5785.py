def solution():
    total_books = 35  # There are 35 books on the cart
    fiction_books = 5  # There are 5 fiction books
    non_fiction_books = fiction_books + 4  # There are 4 more non-fiction books than fiction books
    autobiography_books = fiction_books * 2  # There are 2 times as many autobiographies as fiction books
    picture_books = total_books - fiction_books - non_fiction_books - autobiography_books  # Picture books are the remaining books

    result = picture_books
    return result

print(solution())