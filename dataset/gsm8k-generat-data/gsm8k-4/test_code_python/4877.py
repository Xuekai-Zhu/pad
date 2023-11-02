def solution():
    """Brianna reads two books a month. This year, she was given six new books as a gift, she bought eight new books, and she plans to borrow two fewer new books than she bought from the library. How many of her old books from her old book collection will she have to reread to have two books to read a month this year?"""
    
    # Define the number of books Brianna read per month
    books_per_month = 2

    # Define the number of new books Brianna received as gifts and bought
    new_books = 6 + 8 

    # Define the number of new books Brianna borrowed from the library
    borrowed_books = 8 - 2

    # Calculate the total number of books Brianna has to read this year
    total_books = books_per_month * 12 + new_books + borrowed_books

    # Calculate the number of books Brianna has to reread
    reread_books = total_books - 2 * 12

    result = reread_books
    return result

print(solution())