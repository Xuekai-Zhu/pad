def solution():
    """Nancy, the librarian, is shelving books from the cart. She shelved 12 history books, 8 romance books, and 4 poetry books from the top section of the cart. Half the books on the bottom section of the cart were mystery books, which she quickly put back into place. Then, she shelved the remaining books from the bottom of the cart, including 5 Western novels and 6 biographies. How many books did she have on the book cart when she started?"""
    # Define the number of history, romance, and poetry books on the top section
    top_books = 12 + 8 + 4

    # Define the number of Western novels and biographies on the bottom section
    bottom_books = 5 + 6

    # Define the ratio of mystery books on the bottom section
    mystery_ratio = 1/2

    # Calculate the total number of books on the bottom section
    bottom_total = bottom_books / (1 - mystery_ratio)

    # Calculate the total number of books on the cart
    total_books = top_books + bottom_total

    result = total_books
    return result

print(solution())