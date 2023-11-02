def solution():
    old_books = 2
    new_books_as_gift = 6
    new_books_bought = 8
    new_books_from_library = new_books_bought - 2
    total_new_books = new_books_as_gift + new_books_bought + new_books_from_library
    reads_per_month = 2
    total_reads_needed = total_new_books + old_books
    old_books_to_reread = total_reads_needed - old_books
    result = old_books_to_reread
    return result

print(solution())