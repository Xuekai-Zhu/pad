def solution():
    # Calculate the number of books left after Wednesday
    wednesday_books_left = 98 - 43

    # Calculate the number of books after Thursday
    thursday_books = wednesday_books_left + 23 - 5

    # Calculate the number of books after Friday
    friday_books = thursday_books + 7

    result = friday_books
    return result

print(solution())