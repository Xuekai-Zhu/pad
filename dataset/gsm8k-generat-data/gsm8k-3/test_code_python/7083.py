def solution():
    """Lois has 40 books. She gives a fourth of her books to her nephew. From her remaining books, she donates a third of her books to the library. Then she purchases 3 new books from the book store. How many books does Lois have now?"""
    # Define the initial number of books
    num_books = 40

    # Calculate the number of books given to the nephew
    books_to_nephew = num_books // 4

    # Calculate the number of remaining books
    remaining_books = num_books - books_to_nephew

    # Calculate the number of books donated to the library
    books_to_library = remaining_books // 3

    # Calculate the final number of books
    final_num_books = remaining_books - books_to_library + 3

    # Display the final number of books
    result = final_num_books
    return result

print(solution())