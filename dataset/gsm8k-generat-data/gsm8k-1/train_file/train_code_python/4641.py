def solution():
    """Mcgregor and Floyd were assigned 89 books to read for the week. If Mcgregor was able to finish 34 while Floyd was able to finish 32, how many books do they still have to read?"""
    total_books = 89
    books_read_by_mcgregor = 34
    books_read_by_floyd = 32
    books_to_read = total_books - (books_read_by_mcgregor + books_read_by_floyd)
    result = books_to_read
    return result

print(solution())