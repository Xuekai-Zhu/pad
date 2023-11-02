def solution():
    """A bookseller sells 15 books in January, 16 in February and a certain number of books in March. If the average number of books he sold per month across all three months is 16, how many books did he sell in March?"""
    # Define the number of books sold in January and February
    january_books = 15
    february_books = 16

    # Calculate the total number of books sold across all three months
    total_books = (january_books + february_books + 16) # Average number of books sold per month is 16

    # Calculate the number of books sold in March
    march_books = total_books - january_books - february_books

    result = march_books
    return result

print(solution())