def solution():
    # Define the total number of books assigned
    total_books = 89

    # Define the number of books each person finished
    mcgregor_books = 34
    floyd_books = 32

    # Calculate the total number of books finished
    total_finished = mcgregor_books + floyd_books

    # Calculate the number of books still left to read
    books_left = total_books - total_finished
    result = books_left
    return result

print(solution())