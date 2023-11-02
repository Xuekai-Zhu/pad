def solution():
    """The time Juan takes to grab his lunch from his office and back is half the time he takes to read a book. If he has a 4000-page book, how many pages does he read in an hour if he takes 4 hours to move from his office to grab lunch?"""
    # Define the variables
    lunch_time = 4
    book_time = lunch_time * 2
    book_pages = 4000

    # Calculate the total hours Juan spends reading the book
    total_book_hours = book_time * book_pages / book_time

    # Calculate the number of pages Juan reads in one hour
    pages_per_hour = book_pages / total_book_hours

    result = pages_per_hour
    return result

print(solution())