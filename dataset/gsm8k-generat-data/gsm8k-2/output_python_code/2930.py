def solution():
    """A class has 500 tables and 2/5 times as many books as the number of tables in the class are on top of each table. What's the total number of books in the class?"""
    num_tables = 500
    num_books_per_table = 2/5
    num_books = num_tables * num_books_per_table
    result = num_books
    return result

print(solution())