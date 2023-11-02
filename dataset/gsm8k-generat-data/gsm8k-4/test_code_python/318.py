def solution():
    """Roselyn gives Mara three times as many books as she gives Rebecca and remains with 60 books. If Rebecca received 40 books, how many books did Roselyn have before?"""
    # Define the number of books Rebecca received
    rebecca_books = 40

    # Calculate the number of books remaining with Roselyn
    roselyn_books = 60

    # Calculate the number of books Roselyn gave to Mara
    mara_books = roselyn_books - (rebecca_books * 3)

    # Calculate the total number of books Roselyn had before
    roselyn_total_books = rebecca_books + mara_books + roselyn_books

    # Return the result
    result = roselyn_total_books
    return result

print(solution())