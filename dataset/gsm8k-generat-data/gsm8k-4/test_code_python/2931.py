def solution():
    """A class has 500 tables and 2/5 times as many books as the number of tables in the class are on top of each table. What's the total number of books in the class?"""
    # Define the number of tables and the fraction of books on each table
    num_tables = 500
    fraction_books_per_table = 2/5

    # Calculate the total number of books in the class
    total_books = num_tables * fraction_books_per_table * 10

    # Return the result
    result = total_books
    return result

print(solution())