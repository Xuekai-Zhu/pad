def solution():
    """Peter has 20 books. He has read 40% of them. His brother has read 10% of them. How many more of these books has Peter read than his brother?"""
    # Define the number of books Peter has and the percentage he has read
    peter_books = 20
    peter_percent = 0.4

    # Calculate the number of books Peter has read
    peter_read = peter_books * peter_percent

    # Define the percentage Peter's brother has read
    brother_percent = 0.1

    # Calculate the number of books Peter's brother has read
    brother_read = peter_books * brother_percent

    # Calculate the difference in the number of books Peter and his brother have read
    diff = peter_read - brother_read

    # Display the difference
    result = diff
    return result

print(solution())