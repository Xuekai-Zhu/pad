def solution():
    """Peter has 20 books. He has read 40% of them. His brother has read 10% of them. How many more of these books has Peter read than his brother?"""
    # Define the number of books and the percentage read by Peter and his brother
    total_books = 20
    peter_percent = 0.4
    brother_percent = 0.1

    # Calculate the number of books read by Peter and his brother
    peter_books = total_books * peter_percent
    brother_books = total_books * brother_percent

    # Calculate the difference in the number of books read by Peter and his brother
    diff_books = peter_books - brother_books

    # Return the result
    result = diff_books
    return result

print(solution())