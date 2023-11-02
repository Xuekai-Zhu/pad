def solution():
    """There are 10 books on the table. Two-fifths of them are reading books and three-tenths of them are math books. There is one fewer science book than math books and the rest are history books. How many history books are there?"""
    # Define the total number of books and the fractions of each type
    total_books = 10
    reading_fraction = 2/5
    math_fraction = 3/10

    # Calculate the number of reading and math books
    reading_books = round(total_books * reading_fraction)
    math_books = round(total_books * math_fraction)

    # Calculate the number of science book and the number of history books
    science_books = math_books - 1
    history_books = total_books - reading_books - math_books - science_books

    # Return the number of history books
    result = history_books
    return result

print(solution())