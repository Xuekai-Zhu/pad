def solution():
    # Calculate how many books Evan owns now
    current_books = 200 - 2 - 40  # Evan had 200 books 2 years ago and now owns 40 fewer books

    # Calculate how many books Evan will have in five years
    future_books = 5 * current_books + 60

    # Calculate the total number of books Evan will have in five years
    total_books = current_books + future_books
    result = total_books
    return result

print(solution())