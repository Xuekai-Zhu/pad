def solution():
    """The time Juan takes to grab his lunch from his office and back is half the time he takes to read a book. If he has a 4000-page book, how many pages does he read in an hour if he takes 4 hours to move from his office to grab lunch?"""
    time_to_lunch = 4
    total_time = time_to_lunch * 2
    time_to_read_book = total_time
    pages_in_book = 4000
    pages_per_hour = pages_in_book / time_to_read_book
    result = pages_per_hour
    return result

print(solution())