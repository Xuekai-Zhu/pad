def solution():
    num_rows = 6
    num_columns = 6
    books_per_row = 2 * num_rows + 20

    # Calculate the total number of books needed
    total_books = num_rows * books_per_row
    result = total_books
    return result

print(solution())