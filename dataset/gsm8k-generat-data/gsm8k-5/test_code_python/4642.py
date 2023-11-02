def solution():
    total_books = 89  # The total number of books assigned was 89
    books_read_by_mcgregor = 34  # Mcgregor finished reading 34 books
    books_read_by_floyd = 32  # Floyd finished reading 32 books

    # Calculate the number of books they still have to read
    books_left = total_books - (books_read_by_mcgregor + books_read_by_floyd)
    result = books_left
    return result

print(solution())