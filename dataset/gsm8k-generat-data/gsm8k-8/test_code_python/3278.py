def solution():
    # Calculate Corey's number of books on Tuesday
    mike_books = 45
    corey_books = 2 * mike_books

    # Calculate the number of books Mike gave to Lily on Wednesday
    mike_gave = 10
    corey_gave = mike_gave + 15

    # Calculate Lily's total number of books on Wednesday after receiving books from Mike and Corey
    lily_books = mike_books - mike_gave + corey_books - corey_gave
    result = lily_books
    return result

print(solution())