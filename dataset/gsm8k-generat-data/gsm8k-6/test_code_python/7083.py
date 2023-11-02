def solution():
    # Calculate the number of books Lois gives to her nephew
    nephew_books = 40 / 4  

    # Calculate the number of books Lois has after giving some to her nephew
    remaining_books = 40 - nephew_books  

    # Calculate the number of books Lois donates to the library
    library_books = remaining_books / 3  

    # Calculate the number of books Lois has after donating some to the library
    remaining_books = remaining_books - library_books  

    # Calculate the number of books Lois has after purchasing some new ones
    total_books = remaining_books + 3  

    result = total_books
    return result

print(solution())