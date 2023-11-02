def solution():
    # Calculate the total number of books given out by Roselyn
    total_books_given = 3 * 40 + 40  # Mara receives three times as many books as Rebecca, who received 40 books, and Roselyn remains with 60 books
    # Calculate the number of books Roselyn had before giving any away
    initial_books = total_books_given + 60
    result = initial_books
    return result

print(solution())