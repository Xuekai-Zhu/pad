def solution():
    total_books = 10
    num_reading_books = total_books * 2 / 5
    num_math_books = total_books * 3 / 10
    num_science_books = num_math_books - 1

    # Calculate the total number of history books
    num_history_books = total_books - num_reading_books - num_math_books - num_science_books
    result = num_history_books
    return result

print(solution())