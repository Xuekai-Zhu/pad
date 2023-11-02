def solution():
    total_supplies = 400
    book_ratio = 7
    pen_ratio = 3

    # Calculate the total ratio
    total_ratio = book_ratio + pen_ratio

    # Calculate the number of books
    num_books = (book_ratio / total_ratio) * total_supplies
    result = num_books
    return result

print(solution())