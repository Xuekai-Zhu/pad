def solution():
    # Set the number of books Rebecca received
    rebecca_books = 40

    # Calculate the number of books Roselyn gave Mara
    mara_books = 3 * rebecca_books

    # Calculate the total number of books Roselyn had before giving any away
    total_books = mara_books + rebecca_books + 60
    result = total_books
    return result

print(solution())