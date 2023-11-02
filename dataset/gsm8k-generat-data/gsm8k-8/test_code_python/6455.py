def solution():
    # Calculate the total number of books Adam needs to fill the bookcase
    total_books_needed = 4 * 20 - 2

    # Calculate the number of books Adam had before his shopping trip
    books_before = 56

    # Calculate the number of books Adam bought
    books_bought = total_books_needed - books_before
    result = books_bought
    return result

print(solution())