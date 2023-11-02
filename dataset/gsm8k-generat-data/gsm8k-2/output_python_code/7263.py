def solution():
    """The capacity of Karson's home library is 400 books. If he currently has 120 books, how many more books does he have to buy to make his library 90% full?"""
    library_capacity = 400
    current_books = 120
    target_percent = 0.9
    target_books = library_capacity * target_percent
    additional_books = target_books - current_books
    result = additional_books
    return result

print(solution())