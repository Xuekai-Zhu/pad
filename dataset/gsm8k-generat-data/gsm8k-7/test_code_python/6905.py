def solution():
    num_books = 20
    peter_percent = 0.4
    brother_percent = 0.1

    # Calculate the number of books Peter has read
    peter_books = num_books * peter_percent

    # Calculate the number of books Peter's brother has read
    brother_books = num_books * brother_percent

    # Calculate the difference in the number of books Peter and his brother have read
    diff_books = peter_books - brother_books
    result = diff_books
    return result

print(solution())