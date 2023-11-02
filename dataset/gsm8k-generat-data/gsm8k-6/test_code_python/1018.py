def solution():
    # Calculate the total number of members in the book club including Ron and his wife
    total_members = 3 * 2 + 5 + 2  

    # Calculate the number of times Ron gets to pick a book in one year
    books_per_year = 52 / total_members  # Assuming the book club meets every week
    rons_books_per_year = books_per_year * 2  # Ron and his wife take turns picking a book
    result = rons_books_per_year
    return result

print(solution())