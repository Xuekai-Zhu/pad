def solution():
    """The library has 9,900 books. Over the summer, they sold some books. If only four sixths of the books are left, how many did they sell?"""
    # Define the total number of books
    total_books = 9900

    # Calculate the number of books left
    books_left = total_books * (4/6)

    # Calculate the number of books sold
    books_sold = total_books - books_left

    # Display the number of books sold
    result = books_sold
    return result

print(solution())