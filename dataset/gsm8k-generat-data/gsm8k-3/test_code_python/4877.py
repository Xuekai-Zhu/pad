def solution():
    """Brianna reads two books a month. This year, she was given six new books as a gift, she bought eight new books, and she plans to borrow two fewer new books than she bought from the library. How many of her old books from her old book collection will she have to reread to have two books to read a month this year?"""
    # Calculate the number of new books Brianna borrowed from the library
    borrowed_new_books = 8 - 2

    # Calculate the total number of new books Brianna has this year
    total_new_books = 6 + 8 + borrowed_new_books

    # Calculate the total number of books Brianna needs to read this year
    total_books = 2 * 12  # 2 books a month for 12 months

    # Calculate the number of old books Brianna needs to reread
    old_books = total_books - total_new_books

    # Display the number of old books Brianna needs to reread
    result = old_books
    return result

print(solution())