def solution():
    """The library has 9,900 books. Over the summer, they sold some books. If only four sixths of the books are left, how many did they sell?"""
    total_books = 9900
    remaining_books = total_books * (4/6)
    sold_books = total_books - remaining_books
    result = sold_books
    return result

print(solution())