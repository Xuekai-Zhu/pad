def solution():
    """Lois has 40 books. She gives a fourth of her books to her nephew. From her remaining books, she donates a third of her books to the library. Then she purchases 3 new books from the book store. How many books does Lois have now?"""
    # Define the initial number of books
    initial_books = 40

    # Calculate the number of books given to her nephew
    nephew_books = initial_books // 4

    # Calculate the number of remaining books
    remaining_books = initial_books - nephew_books

    # Calculate the number of books donated to the library
    library_books = remaining_books // 3

    # Calculate the number of books after donating to the library and purchasing new books
    final_books = remaining_books - library_books + 3

    result = final_books
    return result

print(solution())