def solution():
    """A bookseller sells 15 books in January, 16 in February and a certain number of books in March. If the average number of books he sold per month across all three months is 16, how many books did he sell in March?"""
    # Define the number of books sold in January and February
    JANUARY_SALES = 15
    FEBRUARY_SALES = 16

    # Define the total number of books sold across all three months
    TOTAL_SALES = 16 * 3

    # Calculate the number of books sold in March
    march_sales = TOTAL_SALES - JANUARY_SALES - FEBRUARY_SALES

    # Display the number of books sold in March
    result = march_sales
    return result

print(solution())