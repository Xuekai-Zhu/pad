def solution():
    initial_books = 98  # Suzy had 98 books on Wednesday
    books_checked_out = 43  # 43 books were checked out on Wednesday
    books_returned = 23 - 5 + 7  # 23 books were returned on Thursday, 5 books were checked out, and 7 books were returned on Friday

    # Calculate the total number of books Suzy has now
    total_books = initial_books - books_checked_out + books_returned
    result = total_books
    return result

print(solution())