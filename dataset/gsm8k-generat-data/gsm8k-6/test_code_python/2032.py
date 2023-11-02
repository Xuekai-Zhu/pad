def solution():
    # Initial number of books in the library
    num_books = 250

    # Update the number of books based on Tuesday's transaction
    num_books -= 120

    # Update the number of books based on Wednesday's transaction
    num_books += 35

    # Update the number of books based on Thursday's transaction
    num_books -= 15

    result = num_books
    return result

print(solution())