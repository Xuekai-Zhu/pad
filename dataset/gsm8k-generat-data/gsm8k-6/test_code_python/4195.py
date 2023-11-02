def solution():
    # Calculate the total number of books read by Katy during the summer
    june_books = 8
    july_books = 2 * june_books
    august_books = july_books - 3
    total_books = june_books + july_books + august_books
    result = total_books
    return result

print(solution())