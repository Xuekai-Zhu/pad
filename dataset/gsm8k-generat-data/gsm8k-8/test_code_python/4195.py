def solution():
    # Define the number of books Katy read in June
    june_books = 8

    # Define the number of books Katy read in July (twice as many as June)
    july_books = 2 * june_books

    # Define the number of books Katy read in August (three fewer than July)
    august_books = july_books - 3

    # Calculate the total number of books Katy read during the summer
    summer_books = june_books + july_books + august_books
    result = summer_books
    return result

print(solution())