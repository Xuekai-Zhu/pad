def solution():
    # Calculate the total number of books Matias sold in three days
    books_Tuesday = 7
    books_Wednesday = 3 * books_Tuesday
    books_Thursday = 3 * books_Wednesday
    total_books = books_Tuesday + books_Wednesday + books_Thursday
    result = total_books
    return result

print(solution())