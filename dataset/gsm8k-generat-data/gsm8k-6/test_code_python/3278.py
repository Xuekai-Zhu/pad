def solution():
    # Find Corey's number of books on Tuesday
    mike_books = 45
    corey_books = 2 * mike_books  

    # Find the number of books Lily got on Wednesday
    mike_books_after = mike_books - 10  
    corey_books_given = mike_books_after + 15  
    total_books_given = 10 + corey_books_given  
    result = total_books_given
    return result

print(solution())