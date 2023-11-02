def solution():
    books_read_by_matt_1 = 0
    books_read_by_pete_1 = books_read_by_matt_1 * 2
    books_read_by_matt_2 = books_read_by_matt_1 + (books_read_by_matt_1 * 0.5)
    books_read_by_pete_2 = books_read_by_pete_1 * 2
    total_books_read_by_pete = books_read_by_pete_1 + books_read_by_pete_2
    total_books_read_by_matt = books_read_by_matt_1 + books_read_by_matt_2
    result = total_books_read_by_pete
    return result

print(solution())