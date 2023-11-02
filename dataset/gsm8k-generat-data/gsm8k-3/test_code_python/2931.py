def solution():
    """A class has 500 tables and 2/5 times as many books as the number of tables in the class are on top of each table. What's the total number of books in the class?"""
    # Define the number of tables in the class and the fraction of books on each table
    NUM_TABLES = 500
    BOOKS_PER_TABLE = 2/5

    # Calculate the total number of books
    total_books = NUM_TABLES * BOOKS_PER_TABLE * 10  # 10 books per fraction

    # Display the total number of books
    result = total_books
    return result

print(solution())