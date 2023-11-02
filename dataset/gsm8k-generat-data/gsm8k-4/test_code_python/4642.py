def solution():
    """Mcgregor and Floyd were assigned 89 books to read for the week. If Mcgregor was able to finish 34 while Floyd was able to finish 32, how many books do they still have to read?"""
    # Define the total number of books assigned
    total_books = 89

    # Define the number of books read by McGregor and Floyd
    mcgregor_books_read = 34
    floyd_books_read = 32

    # Calculate the total number of books read
    total_books_read = mcgregor_books_read + floyd_books_read

    # Calculate the number of books remaining
    books_remaining = total_books - total_books_read

    result = books_remaining
    return result

print(solution())