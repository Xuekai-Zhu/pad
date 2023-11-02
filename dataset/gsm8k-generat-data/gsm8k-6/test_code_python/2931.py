def solution():
    # Calculate the number of books on top of each table
    books_per_table = (2/5) * 1  # 2/5 times the number of tables, since we have one table to calculate for
    # Calculate the total number of books in the class
    total_books = books_per_table * 500  # multiply by the number of tables in the class
    result = total_books
    return result

print(solution())