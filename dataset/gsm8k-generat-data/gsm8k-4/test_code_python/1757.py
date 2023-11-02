def solution():
    """Arthur knows that he needs to finish 800 pages of reading over the summer.
    He has read 80% of a 500-page book and 1/5 of a 1000 page book.
    How many more pages does he need to read to meet his goal?"""
    
    # Calculate the number of pages Arthur has read so far
    pages_read = 500 * 0.8 + 1000 * (1/5)

    # Calculate the number of pages he needs to read to reach his goal
    pages_to_read = 800 - pages_read

    result = pages_to_read
    return result

print(solution())