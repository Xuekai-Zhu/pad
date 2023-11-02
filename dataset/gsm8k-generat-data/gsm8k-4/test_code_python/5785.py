def solution():
    """There are 35 books on the cart. There are five fiction books, 4 more non-fiction books than fiction books, 2 times as many autobiographies as fiction books, and the rest picture books. How many books were picture books?"""
    # Define the number of fiction books
    fiction_books = 5

    # Calculate the number of non-fiction books
    nonfiction_books = fiction_books + 4

    # Calculate the number of autobiography books
    autobiographies = 2 * fiction_books

    # Calculate the total number of categorized books
    categorized_books = fiction_books + nonfiction_books + autobiographies

    # Calculate the number of picture books
    picture_books = 35 - categorized_books

    result = picture_books
    return result

print(solution())