def solution():
    books_per_month = 2
    new_books_gift = 6
    new_books_bought = 8
    library_books_borrowed = new_books_bought - 2
    
    # Calculate the total number of new books Brianna has for the year
    total_new_books = new_books_gift + new_books_bought + library_books_borrowed
    
    # Calculate the total number of books Brianna needs for the year
    total_books_needed = 12 * books_per_month
    
    # Calculate the number of old books Brianna needs to reread
    old_books_needed = total_books_needed - total_new_books
    
    result = old_books_needed
    return result

print(solution())