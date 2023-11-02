def solution():
    """The time Juan takes to grab his lunch from his office and back is half the time he takes to read a book. If he has a 4000-page book, how many pages does he read in an hour if he takes 4 hours to move from his office to grab lunch?"""
    # Given information
    time_lunch = 4  # Time taken to grab lunch (in hours)
    time_book = 2 * time_lunch  # Time taken to read the book (in hours)
    pages_book = 4000  # Number of pages in the book
    
    # Calculate the rate of reading (in pages per hour)
    rate = pages_book / time_book
    
    # Display the rate of reading
    result = rate
    return result

print(solution())