def solution():
    # Calculate the number of books in the library after Tuesday, Thursday, and Friday
    books_on_Tuesday = 235 - 227
    books_on_Thursday = books_on_Tuesday + 56
    books_on_Friday = books_on_Thursday - 35
    result = books_on_Friday
    return result

print(solution())