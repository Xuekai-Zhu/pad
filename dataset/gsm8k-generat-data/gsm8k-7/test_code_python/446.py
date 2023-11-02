def solution():
    num_children = 10
    initial_books_per_child = 7
    additional_books = 8

    # Calculate the initial total number of books in the classroom
    initial_total_books = num_children * initial_books_per_child

    # Calculate the new total number of books in the classroom after the teacher brings in more books
    new_total_books = initial_total_books + additional_books

    result = new_total_books
    return result

print(solution())