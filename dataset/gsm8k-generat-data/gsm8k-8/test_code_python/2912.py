def solution():
    # Define the number of books in the top level
    top_level_books = 64

    # Calculate the number of books in the third level
    third_level_books = top_level_books / 0.8

    # Calculate the number of books in the second level
    second_level_books = third_level_books / 0.8

    # Calculate the number of books in the first level
    first_level_books = second_level_books / 0.8

    # Calculate the total number of books in the pyramid
    total_books = top_level_books + third_level_books + second_level_books + first_level_books
    result = total_books
    return result

print(solution())