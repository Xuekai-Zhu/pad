def solution():
    total_books = 35
    num_fiction_books = 5
    num_nonfiction_books = num_fiction_books + 4
    num_autobiography_books = num_fiction_books * 2

    # Calculate the total number of fiction, non-fiction, and autobiography books
    total_specific_books = num_fiction_books + num_nonfiction_books + num_autobiography_books

    # Calculate the number of picture books
    num_picture_books = total_books - total_specific_books
    result = num_picture_books
    return result

print(solution())