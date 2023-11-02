def solution():
    # Calculate the total number of non-picture books
    total_non_picture_books = 5 + (5+4) + 2*5  # 5 fiction books, 4 more non-fiction books than fiction books, 2 times as many autobiographies as fiction books

    # Calculate the number of picture books
    picture_books = 35 - total_non_picture_books  # the rest of the books are picture books

    result = picture_books
    return result

print(solution())