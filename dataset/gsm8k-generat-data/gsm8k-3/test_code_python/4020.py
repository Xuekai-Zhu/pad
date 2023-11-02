def solution():
    """There are 10 books on the table. Two-fifths of them are reading books and three-tenths of them are math books.
    There is one fewer science book than math books and the rest are history books. How many history books are there?"""
    # Define the total number of books
    total_books = 10

    # Calculate the number of reading books
    reading_books = total_books * 2 / 5

    # Calculate the number of math books
    math_books = total_books * 3 / 10

    # Calculate the number of science books
    science_books = math_books - 1

    # Calculate the number of history books
    history_books = total_books - reading_books - math_books - science_books

    # Display the number of history books
    result = history_books
    return result

print(solution())