def solution():
    total_books = 10  # There are 10 books on the table
    reading_books = (2 / 5) * total_books  # Two-fifths of the books are reading books
    math_books = (3 / 10) * total_books  # Three-tenths of the books are math books
    science_books = math_books - 1  # There is one fewer science book than math books
    remaining_books = total_books - reading_books - math_books - science_books  # The rest are history books

    # Calculate the number of history books
    history_books = remaining_books
    result = history_books
    return result

print(solution())