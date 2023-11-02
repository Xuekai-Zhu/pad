def solution():
    """John is a hack author.  He writes a book every 2 months.  He has been writing for 20 years and has earned an average of $30,000 per book.  How much money has he made writing?"""
    # Define the number of books John has written
    BOOKS_WRITTEN = 120

    # Define the average earnings per book
    AVERAGE_EARNINGS_PER_BOOK = 30000

    # Calculate the total earnings
    total_earnings = BOOKS_WRITTEN * AVERAGE_EARNINGS_PER_BOOK

    # Display the total earnings
    result = total_earnings
    return result

print(solution())