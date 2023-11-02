def solution():
    total_books = 100  # The library has a collection of 100 books
    books_borrowed_first_day = 5 * 2  # 5 people borrow 2 books each on the first day
    books_borrowed_second_day = 20  # 20 more books are borrowed on the second day

    # Calculate the total number of books borrowed
    total_borrowed = books_borrowed_first_day + books_borrowed_second_day

    # Calculate the number of remaining books
    remaining_books = total_books - total_borrowed
    result = remaining_books
    return result

print(solution())