def solution():
    """A class has 500 tables and 2/5 times as many books as the number of tables in the class are on top of each table. What's the total number of books in the class?"""
    num_tables = 500
    books_per_table = num_tables * (2/5)
    total_books = num_tables * books_per_table
    result = total_books
    return result

print(solution())