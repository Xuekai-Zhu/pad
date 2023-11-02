def solution():
    """Wendy wants to place 20 more than double the number of books in a shelving system with 6 rows and 6 columns. How many books will she need to carry to complete her task?"""
    rows = 6
    columns = 6
    total_books = (rows * columns) * (2 + 20)
    result = total_books
    return result

print(solution())