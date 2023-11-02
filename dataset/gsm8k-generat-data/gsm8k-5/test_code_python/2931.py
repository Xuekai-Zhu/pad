def solution():
    num_tables = 500  # There are 500 tables in the class
    num_books_per_table = (2/5) * num_tables  # 2/5 times as many books as the number of tables are on top of each table

    # Calculate the total number of books in the class
    total_num_books = num_books_per_table * num_tables
    result = total_num_books
    return result

print(solution())