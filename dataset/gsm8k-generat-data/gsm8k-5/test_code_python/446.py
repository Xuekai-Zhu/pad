def solution():
    children = 10  # There are 10 children in the classroom
    initial_books = 7  # Each child has 7 books initially
    additional_books = 8  # The teacher brings 8 more books to the classroom

    # Calculate the total number of books in the classroom
    total_books = children * initial_books + additional_books
    result = total_books
    return result

print(solution())