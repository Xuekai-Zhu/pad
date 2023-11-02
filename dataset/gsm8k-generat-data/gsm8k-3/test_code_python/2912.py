def solution():
    """Alex is stacking his books in a pyramid. Each level of the pyramid has 80% as many books as the number of books in the previous level. If he makes four levels and the top level has 64 books, how many books are in the pyramid in total?"""
    # Define the number of books in the top level
    top_level = 64

    # Calculate the number of books in the third level
    third_level = top_level / 0.8

    # Calculate the number of books in the second level
    second_level = third_level / 0.8

    # Calculate the number of books in the first level
    first_level = second_level / 0.8

    # Calculate the total number of books in the pyramid
    total_books = top_level + third_level + second_level + first_level

    # Display the total number of books
    result = total_books
    return result

print(solution())