def solution():
    """Cody was reading through his favorite book series. The series was 54 books in total. If Cody read 6 books the first week, and 3 books the second week and then 9 books every week after that. How many weeks did it take Cody to read his series?"""
    # Define the total number of books in the series
    total_books = 54

    # Initialize the variable for the number of weeks it takes to read the series
    weeks = 0

    # Track the number of books read each week until the series is complete
    while total_books > 0:
        if weeks == 0:
            total_books -= 6
        elif weeks == 1:
            total_books -= 3
        else:
            total_books -= 9
        weeks += 1

    # return the result
    result = weeks
    return result

print(solution())