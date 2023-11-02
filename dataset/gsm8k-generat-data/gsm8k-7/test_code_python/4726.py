def solution():
    books_Tue = 7
    books_Wed = 3 * books_Tue
    books_Thu = 3 * books_Wed
    
    # Calculate the total number of books sold
    total_books_sold = books_Tue + books_Wed + books_Thu
    
    result = total_books_sold
    return result

print(solution())