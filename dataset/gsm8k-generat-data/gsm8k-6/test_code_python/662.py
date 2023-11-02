def solution():
    # Calculate the number of books each person has
    harry_books = 50
    flora_books = 2 * harry_books
    gary_books = harry_books // 2

    # Calculate the total number of books they own together
    total_books = harry_books + flora_books + gary_books
    result = total_books
    return result

print(solution())