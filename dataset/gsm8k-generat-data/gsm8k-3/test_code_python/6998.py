def solution():
    """Jo reads at a steady pace. Her current book has 210 pages. Now, she is at page 90. An hour ago, she was at page 60. For how many hours will she be reading the book?"""
    # Calculate how many pages Jo read in the past hour
    pages_read = 90 - 60

    # Calculate how many pages Jo has left to read
    pages_left = 210 - 90

    # Calculate how many hours Jo will be reading the book
    hours = pages_left / pages_read

    # Display the number of hours Jo will be reading
    result = hours
    return result

print(solution())