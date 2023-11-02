def solution():
    total_books = 89
    books_read_by_mcgregor = 34
    books_read_by_floyd = 32

    # Calculate the total number of books left to read by subtracting the books read by McGregor and Floyd from the total number of books
    books_left_to_read = total_books - books_read_by_mcgregor - books_read_by_floyd
    result = books_left_to_read
    return result

print(solution())