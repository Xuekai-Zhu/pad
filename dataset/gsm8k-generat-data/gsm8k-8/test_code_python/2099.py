def solution():
    # Calculate Laura's number of books using the given ratio between Elmo and Laura
    laura_books = 1/3 * 24

    # Calculate Stu's number of books using the given ratio between Laura and Stu
    stu_books = 1/2 * laura_books

    result = stu_books
    return result

print(solution())