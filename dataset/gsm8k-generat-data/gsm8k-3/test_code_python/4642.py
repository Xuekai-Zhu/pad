def solution():
    """Mcgregor and Floyd were assigned 89 books to read for the week. If Mcgregor was able to finish 34 while Floyd was able to finish 32, how many books do they still have to read?"""
    # Define the number of books assigned and the number of books finished by each person
    total_books = 89
    mcgregor_books = 34
    floyd_books = 32

    # Calculate the number of books they still have to read
    books_left = total_books - mcgregor_books - floyd_books

    # Display the number of books left to read
    result = books_left
    return result

print(solution())