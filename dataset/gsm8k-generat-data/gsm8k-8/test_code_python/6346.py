def solution():
    # Calculate the number of days Bill has been reading
    days_reading = 12 - 1

    # Calculate the number of pages Bill has read
    pages_read = 8 * days_reading

    # Calculate the total number of pages in the book
    total_pages = pages_read / (2/3)

    result = total_pages
    return result

print(solution())