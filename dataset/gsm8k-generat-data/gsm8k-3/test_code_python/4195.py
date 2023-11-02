def solution():
    """Katy participated in a summer reading program at her local library. She read 8 books in June, twice as many in July and three fewer in August than she did in July. How many books did Katy read during the summer?"""
    # Define the number of books Katy read in June
    june_books = 8

    # Define the number of books Katy read in July
    july_books = june_books * 2

    # Define the number of books Katy read in August
    august_books = july_books - 3

    # Calculate the total number of books Katy read during the summer
    total_books = june_books + july_books + august_books

    # Display the total number of books Katy read
    result = total_books
    return result

print(solution())