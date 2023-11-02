def solution(): 
    num_new_books_last_year = 50 
    num_new_books_this_year = 3 * num_new_books_last_year 
    num_books_before_new_books_last_year = 100 
     
    # Calculate the total number of books in the library now 
    total_books = num_new_books_last_year + num_new_books_this_year + num_books_before_new_books_last_year
     
    result = total_books 
    return result

print(solution())