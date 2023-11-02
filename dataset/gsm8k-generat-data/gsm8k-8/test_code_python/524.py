def solution():
    total_books = 336
    monday_books_taken = 124
    tuesday_books_brought_back = 22

    # Calculate the total books taken out
    total_books_taken = monday_books_taken

    # Calculate the total books brought back
    total_books_brought_back = tuesday_books_brought_back

    # Calculate the remaining books
    remaining_books = total_books - total_books_taken + total_books_brought_back
    result = remaining_books
    return result

print(solution())