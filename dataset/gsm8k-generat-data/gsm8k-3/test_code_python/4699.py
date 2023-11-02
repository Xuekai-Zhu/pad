def solution():
    """Carlos read 28 books in July and 30 books in August.  He needed to read 100 books during his summer vacation. If Carlos read some of the books in June, calculate the number of books that Carlos read in June to meet his goal?"""
    # Define the number of books read in July and August
    books_july = 28
    books_august = 30

    # Define the total number of books Carlos needs to read
    total_books = 100

    # Calculate the number of books Carlos read in June
    books_june = total_books - books_july - books_august

    # Display the number of books Carlos read in June
    result = books_june
    return result

print(solution())