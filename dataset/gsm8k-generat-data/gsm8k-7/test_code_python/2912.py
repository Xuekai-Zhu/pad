def solution():
    top_level_books = 64
    num_books_level_3 = top_level_books / 0.8  # calculate number of books in level 3
    num_books_level_2 = num_books_level_3 / 0.8  # calculate number of books in level 2
    num_books_level_1 = num_books_level_2 / 0.8  # calculate number of books in level 1
    total_books = top_level_books + num_books_level_3 + num_books_level_2 + num_books_level_1  # calculate total books
    result = total_books
    return result

print(solution())