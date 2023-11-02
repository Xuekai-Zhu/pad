def solution():
    total_books = 336
    books_taken_out = 124
    books_brought_back = 22

    # Calculate the total number of books after Monday
    total_books -= books_taken_out

    # Calculate the total number of books after Tuesday
    total_books += books_brought_back

    result = total_books
    return result

print(solution())