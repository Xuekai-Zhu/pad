def solution():
    # Calculate the number of books Lois gives to her nephew
    num_given = 40 // 4

    # Calculate the number of books Lois has left
    num_left = 40 - num_given

    # Calculate the number of books Lois donates to the library
    num_donated = num_left // 3

    # Calculate the number of books Lois has after the donation and purchase
    num_books = num_left - num_donated + 3

    result = num_books
    return result

print(solution())