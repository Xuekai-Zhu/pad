def solution():
    """Cody was reading through his favorite book series.  The series was 54 books in total. If Cody read 6 books the first week, and 3 books the second week and then 9 books every week after that. How many weeks did it take Cody to read his series?"""
    # Define the number of books read in the first two weeks
    books_read_first_two_weeks = 6 + 3

    # Define the total number of books in the series
    total_books = 54

    # Calculate the number of weeks required to read the series
    weeks = (total_books - books_read_first_two_weeks) / 9 + 2

    # Display the number of weeks
    result = weeks
    return result

print(solution())