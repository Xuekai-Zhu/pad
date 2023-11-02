def solution():
    """Alex is stacking his books in a pyramid. Each level of the pyramid has 80% as many books as the number of books in the previous level. If he makes four levels and the top level has 64 books, how many books are in the pyramid in total?"""
    # Define the initial number of books
    num_books = None

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

    # Return the result
    result = round(total_books)
    return result

print(solution())