def solution():
    """Roselyn gives Mara three times as many books as she gives Rebecca and remains with 60 books. If Rebecca received 40 books, how many books did Roselyn have before?"""
    books_given_to_rebecca = 40
    books_given_to_mara = 3 * books_given_to_rebecca
    total_books = books_given_to_rebecca + books_given_to_mara + 60
    result = total_books
    return result

print(solution())