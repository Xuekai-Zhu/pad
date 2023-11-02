def solution():
    # Define the number of tables
    num_tables = 500

    # Calculate the number of books on each table
    num_books_per_table = 2/5 * num_tables

    # Calculate the total number of books in the class
    total_num_books = num_tables * num_books_per_table
    result = total_num_books
    return result

print(solution())