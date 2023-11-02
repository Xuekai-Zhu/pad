def solution():
    # Calculate the total number of books borrowed on the first day
    first_day_borrowed = 5 * 2  # 5 people borrow 2 books each

    # Calculate the total number of books borrowed on the second day
    second_day_borrowed = 20

    # Calculate the total number of books remaining on the shelf
    remaining_books = 100 - first_day_borrowed - second_day_borrowed
    result = remaining_books
    return result

print(solution())