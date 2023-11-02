def solution():
    """In a classroom, 10 children have 7 books each. Their teacher brings another 8 books to the classroom. How many books are in the classroom altogether?"""
    # Define the number of children and the number of books each child has
    children = 10
    books_per_child = 7

    # Calculate the total number of books before the teacher brings in more
    total_books = children * books_per_child

    # Add the number of books the teacher brings in
    total_books += 8

    # Return the result
    result = total_books
    return result

print(solution())