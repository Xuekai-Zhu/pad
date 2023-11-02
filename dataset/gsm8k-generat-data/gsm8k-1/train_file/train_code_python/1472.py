def solution():
    """
    A bookseller sells 15 books in January, 16 in February and a certain number of books in March.
    If the average number of books he sold per month across all three months is 16,
    how many books did he sell in March?
    """
    total_books_sold = 15 + 16 + x
    avg_books_sold = 16
    # total_books_sold divided by 3 months should be equal to avg_books_sold
    # so we can set up an equation to solve for x
    total_books_sold / 3 = avg_books_sold
    # solving for x
    x = (avg_books_sold * 3) - 31
    result = x
    return result

print(solution())