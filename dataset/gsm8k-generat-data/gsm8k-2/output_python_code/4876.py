def solution():
    """Brianna reads two books a month. This year, she was given six new books as a gift, she bought eight new books, and she plans to borrow two fewer new books than she bought from the library. How many of her old books from her old book collection will she have to reread to have two books to read a month this year?"""
    total_new_books = 6 + 8 + (8 - 2)
    books_to_read = 24 - total_new_books
    books_to_reread = 2 * 12 - books_to_read
    result = books_to_reread
    return result

print(solution())