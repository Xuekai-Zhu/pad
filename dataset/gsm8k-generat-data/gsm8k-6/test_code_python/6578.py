def solution():
    # Calculate the number of books that are left
    books_left = (4/6) * 9900

    # Calculate the number of books that were sold
    books_sold = 9900 - books_left
    result = books_sold
    return result

print(solution())