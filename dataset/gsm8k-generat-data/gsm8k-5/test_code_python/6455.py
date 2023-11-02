def solution():
    books_before_shopping = 56  # Adam had 56 books in his bookcase before shopping
    books_per_shelf = 20  # The bookcase averages 20 books per shelf
    total_shelves = 4  # Adam's bookcase has 4 shelves

    # Calculate the total number of books Adam's bookcase can hold
    total_books_capacity = books_per_shelf * total_shelves

    # Calculate the number of books Adam needs to fill his bookcase
    books_needed = total_books_capacity - books_before_shopping - 2  # Two books left over after filling the bookcase

    result = books_needed
    return result

print(solution())