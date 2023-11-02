def solution():
    total_pages = 381  # Total number of pages in the book
    pages_read = 149  # Number of pages Elliot has already read
    pages_per_day = 20  # Number of pages Elliot reads per day
    days = 7  # Number of days for which Elliot reads

    # Calculate the total number of pages Elliot will read in a week
    pages_in_week = pages_per_day * days

    # Calculate the total number of pages Elliot has left to read
    pages_left = total_pages - pages_read - pages_in_week
    result = pages_left
    return result

print(solution())