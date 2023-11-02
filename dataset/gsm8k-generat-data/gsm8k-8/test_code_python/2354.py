def solution():
    # Calculate the total number of books borrowed on the first day
    day1_books = 5 * 2

    # Calculate the total number of books borrowed on the second day
    day2_books = 20

    # Calculate the total number of books borrowed in both days
    total_borrowed = day1_books + day2_books

    # Calculate the number of books remaining on the shelf
    remaining_books = 100 - total_borrowed
    result = remaining_books
    return result

print(solution())