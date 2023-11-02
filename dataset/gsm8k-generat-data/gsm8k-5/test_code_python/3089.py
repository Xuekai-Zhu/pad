def solution():
    total_books = 99  # Tracy has a total of 99 books
    books_first_week = 0  # Initialize the number of books collected in the first week

    # Loop through all possible numbers of books Tracy could have collected in the first week
    for i in range(1, total_books):
        books_next_five_weeks = i * 10  # Tracy collected ten times as many books in the next five weeks
        total_books_collected = i + books_next_five_weeks  # Total number of books collected
        if total_books_collected == total_books:  # Check if the total number of books collected is equal to 99
            books_first_week = i  # Update the number of books collected in the first week
            break
        
    result = books_first_week
    return result

print(solution())