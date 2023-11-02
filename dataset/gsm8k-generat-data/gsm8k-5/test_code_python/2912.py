def solution():
    top_level = 64  # The top level of the pyramid has 64 books
    level_ratio = 0.8  # Each level has 80% as many books as the previous level
    total_books = top_level  # Start with the number of books in the top level

    # Calculate the number of books in each level, starting from the second level
    for i in range(2, 5):
        books_in_level = total_books * level_ratio
        total_books += books_in_level

    result = round(total_books)  # Round to the nearest whole number
    return result

print(solution())