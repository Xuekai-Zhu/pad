def solution():
    """Brianna reads two books a month. This year, she was given six new books as a gift, she bought eight new books, and she plans to borrow two fewer new books than she bought from the library. How many of her old books from her old book collection will she have to reread to have two books to read a month this year?"""
    books_per_month = 2
    new_books_gifted = 6
    new_books_bought = 8
    new_books_borrowed = new_books_bought - 2
    total_new_books = new_books_gifted + new_books_bought + new_books_borrowed
    total_books_needed = 12 * books_per_month - total_new_books
    old_books_to_reread = total_books_needed - 2
    result = old_books_to_reread
    return result

print(solution())