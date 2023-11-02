def solution():
    """There are 10 books on the table. Two-fifths of them are reading books and three-tenths of them are math books. There is one
    fewer science book than math books and the rest are history books. How many history books are there?"""
    
    total_books = 10
    reading_books = (2/5) * total_books
    math_books = (3/10) * total_books
    science_books = math_books - 1
    history_books = total_books - reading_books - math_books - science_books
    
    result = history_books
    return result

print(solution())