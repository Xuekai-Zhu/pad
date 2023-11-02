def solution():
    # Define the number of fiction books
    fiction_books = 5

    # Calculate the number of non-fiction books
    nonfiction_books = fiction_books + 4

    # Calculate the number of autobiographies
    autobiography_books = 2 * fiction_books

    # Calculate the total number of categorized books
    categorized_books = fiction_books + nonfiction_books + autobiography_books

    # Calculate the number of picture books
    picture_books = 35 - categorized_books

    result = picture_books
    return result

print(solution())