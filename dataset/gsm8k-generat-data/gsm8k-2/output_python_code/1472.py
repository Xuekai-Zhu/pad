def solution():
    """A bookseller sells 15 books in January, 16 in February and a certain number of books in March. If the average number of books he sold per month across all three months is 16, how many books did he sell in March?"""
    jan_books = 15
    feb_books = 16
    total_books = jan_books + feb_books
    avg_books = 16
    march_books = (3 * avg_books) - total_books
    result = march_books
    return result

print(solution())