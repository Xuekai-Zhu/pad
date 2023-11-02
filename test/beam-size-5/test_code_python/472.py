def solution():
    total_spent = 300  # Sarah spent $300 on the books
    book_cost = 15  # Each book costs $15
    num_kids = 4  # Sarah gave an equal number of books to her 4 kids

    # Calculate the total number of books Sarah bought
    total_books = total_spent - book_cost

    # Calculate the number of books each child gets
    num_books_per_child = total_books / num_kids
    result = num_books_per_child
    return result

print(solution())