def solution():
    # Calculate the number of books Lois gives to her nephew
    nephew_books = 40 / 4

    # Calculate the number of books Lois has left
    remaining_books = 40 - nephew_books

    # Calculate the number of books Lois donates to the library
    donated_books = remaining_books / 3

    # Calculate the number of books Lois has after these transactions
    total_books = remaining_books - donated_books + 3 
    result = total_books
    return result

print(solution())