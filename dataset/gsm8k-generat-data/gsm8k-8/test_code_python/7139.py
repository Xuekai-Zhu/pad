def solution():
    # Define the total number of books
    total_books = 400

    # Define the desired number of books per category
    desired_books_per_category = 24

    # Keep dividing the categories in half until each has the desired number of books
    num_divisions = 0
    while total_books > desired_books_per_category:
        total_books /= 2
        num_divisions += 1

    result = num_divisions
    return result

print(solution())